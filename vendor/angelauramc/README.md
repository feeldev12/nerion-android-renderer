# Vendored AngelAuraMC prebuilt binaries

These 4 shared libraries are **unmodified** binaries pulled from AngelAuraMC's
`amethyst-prebuilt-libraries` repo's `kopper_zink` renderer bundle
(`renderers/mesa-libs/libs/kopper_zink/`, commit
`ca883665dae3afeaba80b389d3d70f3ef96c9d82`, the AAR previously named
`kopper-zink-release.aar`). We do not build these ourselves — the 2 Mesa/Zink
files we build ourselves (`libEGL_mesa.so`, `libzink_dri.so`) are produced by
`.github/workflows/renderer-zink-kopper.yml` in this same repo and packaged
alongside this vendored quad.

## Current ABI coverage: arm64-v8a only

Only `arm64-v8a` binaries are vendored here. This matches this project's
existing acceptance-target scope (arm64-v8a is the only ABI that has ever been
verified on real hardware; see `app-launcher`'s own design docs). The other 3
ABIs (`armeabi-v7a`, `x86`, `x86_64`) are **not vendored yet** — no cached
build output for them exists anywhere in this project's history, and the
original source (a GitHub Actions CI artifact from AngelAuraMC's own repo) has
long since expired (Actions artifacts expire after 90 days and require repo
write access to re-generate, which we don't have). Adding the other 3 ABIs is
a follow-up, not fabricated here.

## Files and provenance

| File | sha256 | Upstream project | License |
|---|---|---|---|
| `libglapi.so` | `dd6f6920e6b4e399c47b2a62f7d2a8c6d1f2e292821bebb9973ba09ede982e65` | Mesa 3D Graphics Library (`src/mesa/glapi`) — compiled by AngelAuraMC as part of their Mesa/Zink build, unmodified | **MIT** |
| `libcutils.so` | `04258bb1ccef8f5097ddc32ae1fb2d57142ffc5999e96fa36bfab85e02e9e347` | AngelAuraMC's own minimal rebuild of AOSP `libcutils`, compiled from exactly 2 upstream AOSP source files (`libcutils/trace-dev.cpp`, `libcutils/properties.cpp`, fetched from `android.googlesource.com/platform/system/core` at tag `android-platform-13.0.0_r34`), linked against `-llog` only — not a real device's system `libcutils.so` | **Apache-2.0** |
| `libglxshim.so` | `de28da7dad5c44377e65b1ff3d119a5ac382563b4df427aea6ad5d51121924ec` | [`Swung0x48/GLXShim`](https://github.com/Swung0x48/GLXShim) — a small, original bridging utility (`glXGetProcAddress` shim reading `POJAVEXEC_EGL`) | **UNKNOWN / none declared — see "Open licensing question" below** |
| `libopenal.so` | `49bf1ea336c08ee821e29601f378b7fb75439b93537ccf0ee5db402e04c8a149` | OpenAL Soft (`kcat/openal-soft`), compiled by AngelAuraMC for Android | **LGPL-2 or later** |

## Licensing research (task A2, human approval gate)

Verified directly against each upstream project this session (GitHub/GitLab
API + raw source, not guessed):

1. **`libglapi.so` — CLEAR (MIT).** Mesa's own `src/mesa/glapi/glapi_priv.h`
   carries `SPDX-License-Identifier: MIT` (verified against
   `gitlab.freedesktop.org/mesa/mesa`, project id 176, `main` branch). Mesa's
   own license page (`docs.mesa3d.org/license.html`) confirms "the core Mesa
   library is licensed according to the terms of the MIT license." MIT only
   requires retaining the copyright/license notice — satisfied by this
   README + an accompanying `LICENSE-MIT-mesa.txt` (add before first
   Release).

2. **`libcutils.so` — CLEAR (Apache-2.0), fully source-verified.** Found
   AngelAuraMC's actual build script
   (`renderers/mesa-libs/libs/kopper_zink/builddirs/build_libcutils.sh`) and
   confirmed it compiles exactly `trace-dev.cpp` + `properties.cpp` fetched
   from AOSP's `platform/system/core` at tag `android-platform-13.0.0_r34`.
   Fetched both files directly from `android.googlesource.com` and confirmed
   their license headers: `Licensed under the Apache License, Version 2.0`
   (both files, Copyright The Android Open Source Project). Apache-2.0
   requires retaining the license text + a NOTICE if the upstream ships one —
   AOSP's `system/core` does not ship a NOTICE beyond the per-file headers,
   so the per-file headers are what we reproduce.

3. **`libopenal.so` — CLEAR (LGPL-2 or later), standard dynamic-linking use.**
   `kcat/openal-soft`'s own README states "OpenAL Soft is an LGPL-licensed...
   implementation" and its `COPYING` file is the real GNU Library GPL v2 text
   (verified directly, not just the file name — AngelAuraMC's own bundled
   license file is misleadingly named `OPENAL-SOFT_GPL2` in their asset tree,
   but its actual content, and openal-soft's own COPYING, is LGPL, not GPL).
   Redistributing a compiled, unmodified `libopenal.so` and dynamically
   loading it from a proprietary app is exactly the licensing model LGPL is
   designed for (countless commercial games ship openal-soft this way). We
   should still include the LGPL license text and a link to the exact
   upstream source revision AngelAuraMC built from, to fully satisfy LGPL's
   source-correspondence expectation for the library itself (not our app).

4. **`libglxshim.so` — STILL BLOCKS THE FIRST RELEASE. Genuinely unresolved,
   needs a human call.** `Swung0x48/GLXShim` has **no LICENSE file and no
   README at all** (confirmed via `gh api repos/Swung0x48/GLXShim` — GitHub's
   own license field is `null`, and `contents` listing shows only
   `build.gradle.kts` + `src/`; the `/readme` endpoint 404s, meaning there is
   no README to even carry an informal license statement). Under default
   copyright law, no license means no redistribution rights are actually
   granted, regardless of how small or widely-reused the utility is —
   AngelAuraMC's own README lists it as "Unknown License" too, i.e. they are
   in exactly the same unresolved position we are, not a project that solved
   this. This is a **real legal gap**, not a technicality. Options for a
   human to choose between (not decided here):
   - Ship it anyway on the reasoning that it's a tiny (~one file),
     already-widely-redistributed-by-the-entire-Amethyst/Pojav-lineage
     utility with no known objection ever raised by its author — accept the
     residual risk.
   - Reach out to Swung0x48 directly and ask for explicit permission /a
     LICENSE grant (e.g. open an issue on their repo).
   - Write an original from-scratch replacement implementing the same
     `glXGetProcAddress`-reads-`POJAVEXEC_EGL`-and-`dlopen`s pattern (the
     pattern itself is not copyrightable, only Swung0x48's actual expression
     of it is) — mirrors exactly what this project's own
     `tools/android-glfw-shim/src/glfw_shim.c` already did for PojavLauncher's
     GPLv3 native bridge, for the same reason.

**Until item 4 is resolved, task A4 (cut the first public Release) MUST NOT
run** — see this repo's workflow, which stops at artifact upload and does not
publish a Release.
