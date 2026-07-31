#!/usr/bin/env bash
#
# Regenerate poster frames for every video in videos/.
#
# The poster is what the player shows before playback starts. Without one it
# renders a black rectangle, which is the whole reason these exist.
#
# Run from the repo root:
#
#     bash videos/generate-posters.sh
#
# Then LOOK at the results. The default grab point is 3 seconds in, which is a
# guess: if that frame lands on a splash screen, a transition, or an empty
# editor, add the file to POSTER_OFFSETS below with a better timestamp and
# re-run.
#
# Requires ffmpeg and the real video files (run `git lfs pull` first).

set -euo pipefail

cd "$(dirname "$0")/.."

# Seconds into the video to grab the poster frame from.
DEFAULT_OFFSET=3

# Per-file overrides, for videos where the default frame is a poor thumbnail.
# Format: "<basename without extension>:<seconds>"
POSTER_OFFSETS=(
  # At 3s this is still on the Positron welcome/walkthrough splash screen.
  # 20s is the Python Environment setup dialog, which is what the tutorial is about.
  "tutorial-load-python:20"
  # 3s is a near-empty notebook. 38s is the Data Explorer "Convert to Code"
  # dialog, which is the point of the tutorial.
  "tutorial-filter-python:38"
  # 3s is an empty editor. 17s has the plotnine chart and summary table.
  "tutorial-explore-python:17"
  # 3s is an open "New File" dropdown over an empty editor. 55s is the Data
  # Explorer generating dplyr code against starwars.
  "tutorial-load-r:55"
  # 3s is a sparse Quarto doc. 28s has the rendered ggplot2 chart.
  "tutorial-explore-r:28"
)

offset_for() {
  local name="$1"
  local entry
  for entry in "${POSTER_OFFSETS[@]:-}"; do
    if [ "${entry%%:*}" = "$name" ]; then
      echo "${entry##*:}"
      return
    fi
  done
  echo "$DEFAULT_OFFSET"
}

if ! command -v ffmpeg > /dev/null 2>&1; then
  echo "error: ffmpeg not found. Install it with: brew install ffmpeg" >&2
  exit 1
fi

shopt -s nullglob
videos=(videos/*.mp4)
if [ ${#videos[@]} -eq 0 ]; then
  echo "error: no videos found. Run 'git lfs pull' first." >&2
  exit 1
fi

for f in "${videos[@]}"; do
  name="$(basename "$f" .mp4)"
  out="videos/${name}-poster.jpg"
  offset="$(offset_for "$name")"

  # A pointer stub is a few hundred bytes; a real video is megabytes.
  if [ "$(wc -c < "$f")" -lt 10000 ]; then
    echo "error: $f looks like an LFS pointer stub. Run 'git lfs pull' first." >&2
    exit 1
  fi

  # -ss before -i seeks to the keyframe fast; scale to the widest size the
  # player ever renders at, and -q:v 6 keeps these around 100-150 KB.
  ffmpeg -y -v error -ss "$offset" -i "$f" \
    -frames:v 1 -vf "scale=1600:-2" -q:v 6 "$out"

  printf "%-46s %4d KB  (frame at %ss)\n" \
    "$out" "$(( $(wc -c < "$out") / 1024 ))" "$offset"
done

echo
echo "Done. Now open the .jpg files and check each one is a sensible thumbnail."
