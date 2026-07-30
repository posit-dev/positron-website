#!/usr/bin/env bash
#
# Fixture-based tests for build-llms-bundle.sh.
#
# The bundle script otherwise only ever runs during a real release, against a
# rendered site that needs Quarto >= 1.8 to produce llms output at all. These
# tests stand in for that: each case builds a small fake rendered site, runs the
# script, and asserts on the exit status and the operator-facing message.
#
# Run locally with: scripts/test-build-llms-bundle.sh
#
# Deliberately not `set -e`: most cases assert a non-zero exit.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_SCRIPT="$SCRIPT_DIR/build-llms-bundle.sh"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
cd "$WORK" || exit 1

PASS=0
FAIL=0

report() {
	if [ "$2" = yes ]; then
		printf 'ok   %s\n' "$1"
		PASS=$((PASS + 1))
	else
		printf 'FAIL %s\n' "$1"
		[ -n "${3:-}" ] && printf '     %s\n' "$3"
		FAIL=$((FAIL + 1))
	fi
}

# A minimal rendered site. The llms.txt link form mirrors what Quarto emits for a
# site with site-url set: absolute URLs pointing at the .llms.md variants.
new_site() {
	rm -rf _site
	mkdir -p _site/guides
	cat > _site/llms.txt <<'EOF'
# Positron

## Pages

- [Databot](https://positron.posit.co/databot.llms.md)
- [Setup](https://positron.posit.co/guides/setup.llms.md)
EOF
	printf '# Databot\n\nSee the [extension](https://open-vsx.org/extension/posit/databot).\n' \
		> _site/databot.llms.md
	printf '# Setup\n\nHello.\n' > _site/guides/setup.llms.md
}

# Captures combined output in $OUT and the exit status in $STATUS.
run_bundle() {
	OUT="$("$BUNDLE_SCRIPT" "$@" 2>&1)"
	STATUS=$?
}

expect_ok() {
	local name="$1"
	shift
	run_bundle "$@"
	if [ "$STATUS" -eq 0 ]; then
		report "$name" yes
	else
		report "$name" no "expected success, got exit $STATUS: $OUT"
	fi
}

expect_fail() {
	local name="$1" pattern="$2"
	shift 2
	run_bundle "$@"
	if [ "$STATUS" -eq 0 ]; then
		report "$name" no "expected failure, got exit 0"
	elif ! grep -qF "$pattern" <<<"$OUT"; then
		report "$name" no "exit $STATUS but message lacked '$pattern': $OUT"
	else
		report "$name" yes
	fi
}

echo "== accepted =="

new_site
expect_ok "positron profile builds" _site positron 0.0.0-test

# Artifact shape, checked once on the happy path.
ENTRIES="$(unzip -Z1 positron-llms-0.0.0-test.zip)"
for want in llms.txt bundle.json databot.llms.md guides/setup.llms.md; do
	if grep -qxF "$want" <<<"$ENTRIES"; then
		report "zip contains $want" yes
	else
		report "zip contains $want" no "entries: $(tr '\n' ' ' <<<"$ENTRIES")"
	fi
done

MANIFEST="$(unzip -p positron-llms-0.0.0-test.zip bundle.json)"
DECLARED="$(sed -n 's/.*"fileCount": *\([0-9]*\).*/\1/p' <<<"$MANIFEST")"
ACTUAL="$(grep -vc '/$' <<<"$ENTRIES")"
if [ "$DECLARED" = "$ACTUAL" ]; then
	report "bundle.json fileCount matches zip ($ACTUAL)" yes
else
	report "bundle.json fileCount matches zip" no "declared $DECLARED, zip holds $ACTUAL"
fi

for want in '"schema": 1' '"profile": "positron"' '"version": "0.0.0-test"'; do
	if grep -qF "$want" <<<"$MANIFEST"; then
		report "bundle.json has $want" yes
	else
		report "bundle.json has $want" no "$MANIFEST"
	fi
done

# The rewrite must leave the index pointing inside the bundle.
INDEX="$(unzip -p positron-llms-0.0.0-test.zip llms.txt)"
if grep -qF '(databot.llms.md)' <<<"$INDEX" && ! grep -qF 'positron.posit.co' <<<"$INDEX"; then
	report "llms.txt links are bundle-relative" yes
else
	report "llms.txt links are bundle-relative" no "$INDEX"
fi

if shasum -a 256 -c positron-llms-0.0.0-test.zip.sha256sum > /dev/null 2>&1; then
	report "checksum file verifies" yes
else
	report "checksum file verifies" no ""
fi

new_site
expect_ok "workbench profile builds" _site workbench 0.0.0-test
if [ -f positron-workbench-llms-0.0.0-test.zip ]; then
	report "workbench basename is positron-workbench-llms" yes
else
	report "workbench basename is positron-workbench-llms" no ""
fi

# Regression test for the guard that used to scan every staged file: docs may
# carry absolute site links in prose, and that must not fail the build.
new_site
printf '# Databot\n\nWorks with [Positron](https://positron.posit.co/) and see\n[Packages](https://positron.posit.co/packages-pane).\n' \
	> _site/databot.llms.md
expect_ok "prose site link in a doc is allowed" _site positron 0.0.0-test

new_site
printf -- '- [Databot](https://positron.posit.co/databot.llms.md#usage)\n' >> _site/llms.txt
expect_ok "link with a fragment resolves" _site positron 0.0.0-test

new_site
printf -- '- [Databot](https://positron.posit.co/databot.llms.md?v=2)\n' >> _site/llms.txt
expect_ok "link with a query string resolves" _site positron 0.0.0-test

echo
echo "== rejected =="

new_site
rm _site/llms.txt
expect_fail "missing llms.txt" "llms.txt not found" _site positron 0.0.0-test

new_site
find _site -name '*.llms.md' -delete
expect_fail "no docs rendered" "no *.llms.md files" _site positron 0.0.0-test

new_site
rm _site/databot.llms.md
expect_fail "index links a file not in the bundle" "which is not in the bundle" \
	_site positron 0.0.0-test

new_site
printf -- '- [Root](/databot.llms.md)\n' >> _site/llms.txt
expect_fail "root-relative link" "not bundle-relative" _site positron 0.0.0-test

new_site
printf -- '- [Contact](mailto:docs@posit.co)\n' >> _site/llms.txt
expect_fail "mailto link" "not bundle-relative" _site positron 0.0.0-test

# http:// survives a rewrite that only strips https://, so guard 3 is what fires.
new_site
printf -- '- [Databot](http://positron.posit.co/databot.llms.md)\n' >> _site/llms.txt
expect_fail "site URL the rewrite missed" "still references positron.posit.co" \
	_site positron 0.0.0-test

new_site
expect_fail "unknown profile" "profile must be" _site dailies 0.0.0-test

# The size budget, exercised by shrinking the budget rather than by padding a
# fixture past 1MB. Exported and unset around the call: an assignment prefixing a
# function call stays in effect afterwards in bash, which would silently cap
# every later case.
new_site
export LLMS_BUNDLE_MAX_BYTES=100
expect_fail "zip over the size budget" "over the 100 byte budget" _site positron 0.0.0-test
unset LLMS_BUNDLE_MAX_BYTES

echo
printf '%d passed, %d failed\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ]
