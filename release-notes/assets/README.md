# Release notes assets

Images and GIFs referenced from the release notes (`release.md` and the archived
`release-*.qmd` files) live here so they are version-controlled alongside the
notes that use them.

## How these reach the CDN

When a change under `release-notes/assets/` is merged to `main`, the
[`publish-release-notes-assets.yml`](../../.github/workflows/publish-release-notes-assets.yml)
workflow syncs this directory to S3 and invalidates the CloudFront cache. The
sync is additive: it uploads new or changed files and never deletes existing
ones. You can also run the workflow manually from the Actions tab (for example,
to publish to the `staging` or `dailies` channel) once you have write access.

Because assets publish on merge, you can merge an assets-only change first, then
author the release notes against the live CDN URL and preview the real
rendering.

## Naming and referencing

Name files `<year>-<month>-<slug>.<ext>`, for example `2026-06-posit-assistant.gif`.

Reference them with the absolute CDN URL (not a relative path), centered with a
`<p align="center">` wrapper:

```html
<p align="center"><img src="https://cdn.posit.co/positron/releases/release-notes/assets/2026-06-posit-assistant.gif" alt="Describe the image"></p>
```

This file is excluded from the S3 sync.
