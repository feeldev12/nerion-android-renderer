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

## Unified bundle (what the launcher fetches today)

`renderer-unified-v*` Releases carry every renderer the launcher loads, in one
`renderer-unified-<abi>.tar.xz`. v1 was assembled by hand; v2 is produced by
`.github/workflows/renderer-unified.yml` = v1 unchanged + `libltw.so` built
from a pinned `MojoLauncher/LTW` commit (see `vendor/ltw/README.md`, LGPL-3.0).

## Status

- ABI coverage: `arm64-v8a` only for the vendored quad right now (build
  matrix covers all 4 ABIs for the self-built pair).
- **First public Release is gated on task A2's licensing research for
  `libglxshim.so`** — see `vendor/angelauramc/README.md`. Not published yet.

## License notices

`notices/` holds the notices for every library in the unified bundle:
`THIRD_PARTY_NOTICES.md` (project, source commit, license and copyright of each
`.so`) and the full license texts it points to. `renderer-notices.yml` checks
that each `.so` in the published bundle has its notice
(`scripts/check_notices.py`) and, from `main`, attaches them to the bundle's
Release as `renderer-notices.tar.xz` (+ `.sha256`). The launcher ships the same
files in its APK (`assets/licenses/renderers/`).

`vendor/angelauramc/LICENSE-MIT-mesa.txt` is a saved GitLab "404" page, not the
Mesa license; `notices/LICENSE-Mesa.rst` is the real text (Mesa's
`docs/license.rst` at the pinned commit). The vendor file is left as is because
any change under `vendor/angelauramc/` re-runs `renderer-zink-kopper.yml`, which
republishes its Release.
