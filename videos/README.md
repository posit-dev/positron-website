# Videos

Videos embedded in the site live here so they are version-controlled alongside
the pages that use them. They are stored with Git LFS (see `.gitattributes`), so
make sure LFS is installed and initialized (`git lfs install`) before adding or
replacing one.

The site does **not** serve these files. Netlify excludes them from the build
output (`"!videos/**"` in `_quarto.yml`),
and pages load them from the CDN instead.

## How these reach the CDN

When a change under `videos/` is merged to `main`, the
[`publish-videos.yml`](../.github/workflows/publish-videos.yml) workflow syncs
this directory to S3 and invalidates the CloudFront cache. The sync is additive:
it uploads new or changed files and never deletes existing ones. You can also
run the workflow manually from the Actions tab once you have write access.

Videos publish to the `releases` channel only. They are evergreen and identical
across channels, so the dailies build references these same URLs.

Because assets publish on merge, **a PR that adds a new video will show a broken
player in its Netlify preview** until the change lands on `main`. Merge the
video first, then write the page that uses it, the same way
`release-notes/assets/` works.

## Referencing a video

Use the [`cdn-video` shortcode](../_extensions/cdn-video/), writing the video
and poster URLs out in full:

```
{{< cdn-video https://cdn.posit.co/positron/releases/videos/example.mp4
  poster="https://cdn.posit.co/positron/releases/videos/example-poster.jpg"
  aria-label="Describe what the video shows" >}}
```

Both URLs are explicit on purpose. Nothing is rewritten between the source and
the rendered page, so what you read here is exactly what the browser requests
and both URLs are greppable. This matches how `release-notes/assets/` are
referenced.

`poster` and `aria-label` are both required. The build fails with an explanatory
error if either is missing: without a poster the player renders a black
rectangle, and `aria-label` is the only description a screen reader gets.

`preload` is not set per-video. It is a single site-wide knob, `video-preload`
in `_quarto-positron.yml`, currently `"none"` so that videos stay off the
critical path and the poster is what visitors see until they click play.

Do not use Quarto's built-in `{{< video >}}` shortcode. It injects video.js,
569 KB of render-blocking JavaScript, into the page head. The `cdn-video`
shortcode emits a native HTML5 `<video>` element instead and loads no
JavaScript at all.

## Poster frames

Every video needs a matching `<name>-poster.jpg`, which is what the player shows
before playback starts. Without one the player renders a black rectangle.
Regenerate them with:

```bash
bash videos/generate-posters.sh
```

The script grabs a frame 3 seconds in. Check the result: if that frame lands on a
splash screen, a transition, or an empty editor, pick a better timestamp for that
file by hand and commit the replacement.

## Replacing an existing video

Keep the filename stable so no page references need updating. Note that objects
are published with a one week `max-age`. The workflow invalidates CloudFront, so
edge caches update immediately, but a browser that already downloaded the old
file may keep serving it for up to a week.

## Encoding guidance

These are delivered over a CDN and played in a player roughly 1000px wide, so
source-quality screen recordings are heavily oversized. Before adding a video:

- Cap the width at 1600px and the frame rate at 30fps
- Drop the audio track (`-an`) unless the video actually has narration; several
  of these carried silent audio tracks costing close to a megabyte each
- Use `-movflags +faststart` so playback can begin before the full file arrives

```bash
ffmpeg -i input.mp4 -vf "scale=1600:-2,fps=30" \
  -c:v libx264 -crf 28 -preset slow -profile:v high -pix_fmt yuv420p \
  -an -movflags +faststart videos/output.mp4
```

Do not tune by file size alone. Extract a frame from a text-heavy region and
look at it. These videos exist to show how Positron renders text, and
compression artifacts on UI text are exactly what makes them look bad.

This file and `generate-posters.sh` are excluded from the S3 sync.
