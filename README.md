# nerion-android-renderer

Builds and publishes the GLES-on-Android renderer bundle (Mesa/Zink "kopper")
consumed by [`feeldev12/launcher`](https://github.com/feeldev12/launcher)'s
build-time `fetchRendererLibs` Gradle task. Separate from
[`nerion-android-jdk-build`](https://github.com/feeldev12/nerion-android-jdk-build),
mirroring AngelAuraMC's own `angelauramc-openjdk-build` /
`amethyst-prebuilt-libraries` split (independent cadence, size, and licensing
surface per artifact).

## What this produces

A per-ABI `.tar.xz` (+ `.sha256`) containing exactly 6 shared libraries:

- `libEGL_mesa.so`, `libzink_dri.so` — built by this repo's own CI
  (`.github/workflows/renderer-zink-kopper.yml`) from a pinned
  [`Swung0x48/mesa`](https://gitlab.freedesktop.org/Swung0x48/mesa) fork
  commit.
- `libglapi.so`, `libcutils.so`, `libglxshim.so`, `libopenal.so` — vendored,
  unmodified prebuilt binaries (`vendor/angelauramc/<abi>/`) — see that
  directory's own README for full provenance and licensing research.

## Status

- ABI coverage: `arm64-v8a` only for the vendored quad right now (build
  matrix covers all 4 ABIs for the self-built pair).
- **First public Release is gated on task A2's licensing research for
  `libglxshim.so`** — see `vendor/angelauramc/README.md`. Not published yet.
