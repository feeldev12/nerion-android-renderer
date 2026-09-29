# LTW (Large Thin Wrapper)

`libltw.so` is **built by this repo's CI**, not vendored as a binary:
`.github/workflows/renderer-unified.yml` checks out
[`MojoLauncher/LTW`](https://github.com/MojoLauncher/LTW) at a pinned commit,
runs the upstream build (`./gradlew :ltw:assembleRelease`, NDK
`28.2.13676358` as set by upstream's `ltw/build.gradle`) and takes
`jni/<abi>/libltw.so` from the resulting AAR, unmodified.

| | |
|---|---|
| Upstream | https://github.com/MojoLauncher/LTW |
| Pinned commit | `11f1b36f701e69731d685e94c6788e60d829ea35` ("Feat[ltw]: add Mojo to GL_VENDOR string") |
| License | **LGPL-3.0** — full text in `LICENSE-LGPL-3.0-ltw.txt` (copied from upstream at the pinned commit) |
| Used by | the launcher's `Ltw` renderer (`opengles_ltw`), loaded as `libltw.so` |

## Why it's built, not vendored

Upstream publishes no releases, only 90-day CI artifacts. Building from a
pinned commit keeps the binary reproducible and gives the exact
corresponding source that LGPL-3.0 requires us to point to.

## LGPL-3.0 obligations

`libltw.so` is shipped as its own shared library, dynamically loaded, so users
can replace it — which is what LGPL-3.0 section 4 asks of a combined work.
Distributing it also means passing along the license text and a pointer to
the corresponding source (the upstream repo at the pinned commit above).

## Bumping LTW

Change `LTW_REF` in `renderer-unified.yml` and the commit in this README,
re-copy `LICENSE` if it changed, then publish under a new `RELEASE_TAG` and
bump `renderer.tag`/`renderer.version` in the launcher's
`src-tauri/gen/android/app/renderer.properties`.
