#!/usr/bin/env bash
#
# Build the slim LLM-only docs bundle from a rendered Quarto site.
#
# Emits <basename>-<version>.zip and <basename>-<version>.zip.sha256sum in the
# current directory, where <basename> is positron-llms or positron-workbench-llms.
#
# Every guard here is load-bearing: the bundle is consumed by Positron's
# parseManifest(), which rejects anything it does not recognise, so a bad
# bundle must fail this workflow rather than ship.
set -euo pipefail

SITE_DIR="${1:?usage: build-llms-bundle.sh <site-dir> <profile> <version>}"
PROFILE="${2:?usage: build-llms-bundle.sh <site-dir> <profile> <version>}"
VERSION="${3:?usage: build-llms-bundle.sh <site-dir> <profile> <version>}"

# Bump only when a schema-1 reader would misread the bundle. See the design
# spec's "Schema versioning policy" section before changing this.
SCHEMA=1
DOCS_BASE_URL="https://positron.posit.co/"

case "$PROFILE" in
	positron)  BASENAME="positron-llms" ;;
	workbench) BASENAME="positron-workbench-llms" ;;
	*) echo "error: profile must be 'positron' or 'workbench', got '$PROFILE'" >&2; exit 1 ;;
esac

ZIP_NAME="${BASENAME}-${VERSION}.zip"
# Captured before any `cd`: the zip is written here, and step 6 zips from inside
# $STAGE, so a relative path or $OLDPWD would resolve against the wrong dir.
OUT_DIR="$PWD"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

if [ ! -f "$SITE_DIR/llms.txt" ]; then
	echo "error: $SITE_DIR/llms.txt not found; did the Quarto render run?" >&2
	exit 1
fi

# 1. Copy llms.txt and every *.llms.md, preserving directory structure.
# A tar pipe rather than `cp --parents`: that flag is GNU-only, and this script
# must run on a contributor's macOS checkout as well as the Linux runner.
cp "$SITE_DIR/llms.txt" "$STAGE/llms.txt"
( cd "$SITE_DIR" && find . -name '*.llms.md' -type f -print0 | tar -cf - --null -T - ) \
	| ( cd "$STAGE" && tar -xf - )

# 2. Rewrite llms.txt to bundle-relative paths. This is what schema 1 promises.
# Write-and-move rather than `sed -i`: in-place editing needs no suffix on GNU
# sed and a mandatory one on BSD, so no single `-i` spelling is portable.
sed "s|${DOCS_BASE_URL}||g" "$STAGE/llms.txt" > "$STAGE/llms.txt.rewritten"
mv "$STAGE/llms.txt.rewritten" "$STAGE/llms.txt"

# 3. Guard: no bundled file may still reference the site.
if grep -rl 'positron\.posit\.co' "$STAGE" ; then
	echo "error: bundled files still reference positron.posit.co (listed above)." >&2
	echo "The rewrite assumes only llms.txt carries site links. That assumption broke." >&2
	exit 1
fi

# 4. Guard: every link in llms.txt must now be bundle-relative.
if grep -oE '\]\([^)]+\)' "$STAGE/llms.txt" | grep -E '\((https?:)?//' ; then
	echo "error: llms.txt still contains absolute links (listed above)." >&2
	exit 1
fi

FILE_COUNT="$(find "$STAGE" -type f | wc -l | tr -d ' ')"

# 5. Generate bundle.json, then include it in the count it reports.
cat > "$STAGE/bundle.json" <<JSON
{
  "schema": ${SCHEMA},
  "profile": "${PROFILE}",
  "version": "${VERSION}",
  "generated": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "docsBaseUrl": "${DOCS_BASE_URL}",
  "fileCount": $((FILE_COUNT + 1))
}
JSON

# 6. Zip, then verify the archive round-trips the guards.
rm -f "$ZIP_NAME"
( cd "$STAGE" && zip -q -r -X "$OUT_DIR/$ZIP_NAME" . )

# Read the entry list once into a variable rather than piping `unzip` into
# `grep -q` per check. Under `set -o pipefail` a `grep -q` that matches early
# can close the pipe before `unzip` finishes writing, and the resulting SIGPIPE
# (141) fails the pipeline even though the archive is fine.
ENTRIES="$(unzip -Z1 "$ZIP_NAME")"

grep -qx 'llms.txt' <<<"$ENTRIES"    || { echo "error: zip missing llms.txt" >&2; exit 1; }
grep -qx 'bundle.json' <<<"$ENTRIES" || { echo "error: zip missing bundle.json" >&2; exit 1; }

# `grep -c` exits 1 on a zero count, which `set -e` would treat as fatal, so
# tolerate it and let the comparison below report the real mismatch.
ZIPPED_COUNT="$(grep -vc '/$' <<<"$ENTRIES" || true)"
DECLARED_COUNT="$((FILE_COUNT + 1))"
if [ "$ZIPPED_COUNT" -ne "$DECLARED_COUNT" ]; then
	echo "error: zip holds $ZIPPED_COUNT files but bundle.json declares $DECLARED_COUNT" >&2
	exit 1
fi

# 7. Digest sidecar. Positron refuses to extract without a matching one.
shasum -a 256 "$ZIP_NAME" > "${ZIP_NAME}.sha256sum"
shasum -a 256 -c "${ZIP_NAME}.sha256sum"

echo "built $ZIP_NAME ($(wc -c < "$ZIP_NAME") bytes, $DECLARED_COUNT files) + sidecar"
