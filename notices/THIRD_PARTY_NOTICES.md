# Third-party notices: Android renderer bundle

These are the notices for the 13 shared libraries in the `renderer-unified-arm64-v8a.tar.xz`
bundle that [feeldev12/nerion-android-renderer](https://github.com/feeldev12/nerion-android-renderer)
publishes (release `renderer-unified-v3`) and that the Nerion launcher for Android ships in its
APK. None of them is part of the launcher's own code. Each one is a separate shared library that
the launcher loads at run time (`dlopen`) only when the player picks that renderer.

The full license texts are in the files next to this one. Every library is listed with the
project, the exact source commit, the license and the copyright holders.

## Libraries under the LGPL: source code and replacing them

`libltw.so` (LGPL-3.0), `libmobileglues.so` (LGPL-2.1) and `libopenal.so` (LGPL-2.0 or later)
are covered by the GNU Lesser/Library General Public License:

- They are distributed unmodified, built from the exact source commits below. That source is
  public at those links, and you can get it there for as long as this version is distributed.
  If a link stops working, write to the launcher's developer through the support channels on
  the Nerion website and you'll get a copy of the same source.
- Each one is a separate shared library loaded dynamically at run time. The launcher doesn't
  link them statically or change them, so you can replace any of them with your own build of
  the same library (for example with a modified version) and the launcher will load it in its
  place.
- LGPL-3.0 is a set of additional permissions on top of the GNU GPL version 3, so both texts
  are included (`LICENSE-LGPL-3.0.txt`, `LICENSE-GPL-3.0.txt`).

---

## `libltw.so`: LTW (Large Thin Wrapper)

- Project: LTW, a thin OpenGL core to OpenGL ES wrapper
- Source: https://github.com/MojoLauncher/LTW/tree/11f1b36f701e69731d685e94c6788e60d829ea35
- Commit: `11f1b36f701e69731d685e94c6788e60d829ea35`
- Built by: this repo's `renderer-unified.yml` for `renderer-unified-v2` (run 36547107142,
  `./gradlew :ltw:assembleRelease`, unmodified); v3 carries that same binary
- License: LGPL-3.0 (`LICENSE-LGPL-3.0.txt`, `LICENSE-GPL-3.0.txt`)
- Copyright (c) 2025 artDev, SerpentSpirale, CADIndie
- Includes a GLSL optimizer derived from Mesa (`ltw/src/main/tinywrapper/glsl_optimizer`),
  MIT (`LICENSE-Mesa.rst`).

## `libmobileglues.so`: MobileGlues

- Project: MobileGlues, an OpenGL to OpenGL ES translation layer
- Source: https://github.com/MobileGL-Dev/MobileGlues/tree/311b9e5ad1e4556dbdf15173e001aed9411bf977
- Commit: `311b9e5ad1e4556dbdf15173e001aed9411bf977` (MobileGlues 1.3.4)
- Built by: this repo's `renderer-unified.yml`, with the recipe of
  AngelAuraMC/amethyst-prebuilt-libraries@`ca883665dae3afeaba80b389d3d70f3ef96c9d82`
- License: LGPL-2.1 (`LICENSE-LGPL-2.1-MobileGlues.txt`)
- Copyright (c) 2025-2026 MobileGL-Dev
- Bundled third-party code (pinned by that commit):
  - SPIRV-Cross, KhronosGroup/SPIRV-Cross@`a0fba56c34a6700f1724bf9b751da5b488a3775c`:
    Apache-2.0 (`LICENSE-Apache-2.0.txt`)
  - glslang, KhronosGroup/glslang@`f5f664dee8146676b04a332a7233959fc3ce9681`: BSD-3-Clause,
    MIT, Apache-2.0 and others (`LICENSE-glslang.txt`)
  - GLM, g-truc/glm@`e7970a8b26732f1b0df9690f7180546f8c30e48e`: Happy Bunny License or MIT
    (`LICENSE-GLM.txt`), Copyright (c) 2005 G-Truc Creation
  - xxhash, stbrumme/xxhash@`c2866db364b6ea3a11933e62235ddc166ba18565`: MIT
    (`LICENSE-MIT.txt`), Copyright (c) 2018 Stephan Brumme
  - cJSON: MIT (`LICENSE-MIT.txt`), Copyright (c) 2009-2017 Dave Gamble and cJSON contributors
  - FidelityFX Super Resolution 1.0 shaders: MIT (`LICENSE-MIT.txt`), Copyright (c) 2021
    Advanced Micro Devices, Inc.; Copyright (c) 2014 Michal Drobot
  - FastSTL, MobileGL-Dev/FastSTL@`644b3b01e6e7dcb6a67818289d2fb9bbe85232f2`, by the same
    authors as MobileGlues (no separate license declared)

## `libopenal.so`: OpenAL Soft

- Project: OpenAL Soft 1.24.3, 3D audio library
- Source: https://github.com/AngelAuraMC/openal-soft/tree/1e3764ed0622195b9fa1b67982daf93f5736420d
  (AngelAuraMC's fork of https://github.com/kcat/openal-soft)
- Commit: `1e3764ed0622195b9fa1b67982daf93f5736420d`, as pinned by
  AngelAuraMC/amethyst-prebuilt-libraries@`ca883665dae3afeaba80b389d3d70f3ef96c9d82`
- Built by: AngelAuraMC; vendored unmodified (`vendor/angelauramc/`)
- License: LGPL-2.0 or later (GNU Library General Public License v2,
  `LICENSE-LGPL-2.0-OpenAL-Soft.txt`). Portions under BSD-3-Clause
  (`LICENSE-BSD-3-Clause-OpenAL-Soft.txt`) and the PFFFT license (`LICENSE-pffft-OpenAL-Soft.txt`).
- Copyright (C) 1999-2007 by authors (OpenAL Soft contributors); Copyright (c) 2015 Archontis
  Politis; Copyright (c) 2019 Anis A. Hireche; Copyright (c) 2019 Christopher Robinson

---

## `libEGL_mesa.so`, `libzink_dri.so`: Mesa (Zink, Kopper)

- Project: Mesa 3D Graphics Library, Swung0x48's fork with the Kopper patch for Android
- Source: https://gitlab.freedesktop.org/Swung0x48/mesa/-/tree/9ea0decb3176d34e578c3c603fd9c8e29b580f71
- Commit: `9ea0decb3176d34e578c3c603fd9c8e29b580f71`
- Built by: this repo's `renderer-unified.yml`
- License: MIT (`LICENSE-Mesa.rst`)
- Copyright (C) 1999-2007 Brian Paul; Copyright 2018 Collabora Ltd. (Zink); and the other Mesa
  contributors named in each source file
- Statically links libdrm, https://gitlab.freedesktop.org/mesa/libdrm/-/tree/76a1e97a9a7c29fa3035bb370d654791bdc23d90
  (commit `76a1e97a9a7c29fa3035bb370d654791bdc23d90`): MIT (`LICENSE-MIT.txt`), Copyright 1999
  Precision Insight, Inc.; Copyright 2000 VA Linux Systems, Inc.

## `libglapi.so`: Mesa GL API dispatch

- Project: Mesa 3D Graphics Library (`src/mapi`), same fork and commit as above:
  https://gitlab.freedesktop.org/Swung0x48/mesa/-/tree/9ea0decb3176d34e578c3c603fd9c8e29b580f71
- Commit: `9ea0decb3176d34e578c3c603fd9c8e29b580f71`, as pinned by
  AngelAuraMC/amethyst-prebuilt-libraries@`ca883665dae3afeaba80b389d3d70f3ef96c9d82`
- Built by: AngelAuraMC; vendored unmodified (`vendor/angelauramc/`)
- License: MIT (`LICENSE-Mesa.rst`)
- Copyright (C) 1999-2008 Brian Paul and the Mesa contributors

## `libvulkan_freedreno.so`: Turnip (Mesa Vulkan driver for Adreno)

- Project: Mesa 3D Graphics Library, Turnip driver (`src/freedreno/vulkan`)
- Version: Mesa 25.2.1 (the version string inside the binary)
- Source: https://gitlab.freedesktop.org/mesa/mesa/-/tree/mesa-25.2.1
  (tag `mesa-25.2.1`, commit `d6e3b017b2e38131a4918624c9c3c2792f477a96`)
- Built by: prebuilt binary, added unmodified to `renderer-unified-v1`. Which build it came from
  wasn't recorded, so the commit above is the upstream release that matches its version string,
  not a confirmed build input.
- License: MIT (`LICENSE-MIT.txt`, `LICENSE-Mesa.rst`)
- Copyright (c) 2016 Red Hat; Copyright (c) 2016 Bas Nieuwenhuizen; Copyright (c) 2015 Intel
  Corporation; and the other Mesa contributors

## `libgl4es_115.so`: HolyGL4ES

- Project: HolyGL4ES 1.1.5, OpenGL 2.1 on OpenGL ES (AngelAuraMC's fork of gl4es)
- Source: https://github.com/AngelAuraMC/HolyGL4ES/tree/beada3754693ec0cd492a1580d320474657918d8
- Commit: `beada3754693ec0cd492a1580d320474657918d8`
- Built by: this repo's `renderer-unified.yml`, with the recipe of
  AngelAuraMC/amethyst-prebuilt-libraries@`ca883665dae3afeaba80b389d3d70f3ef96c9d82`
- License: MIT (`LICENSE-MIT.txt`)
- Copyright (c) 2016-2018 Sebastien Chevalier; Copyright (c) 2013-2016 Ryan Hileman

## `libng_gl4es.so`: NG-GL4ES (Krypton Wrapper)

- Project: NG-GL4ES / Krypton Wrapper 0.4.5
- Source: https://github.com/BZLZHH/NG-GL4ES/tree/6e153a1622a8d9ef903f7975aafbef2453571bab
- Commit: `6e153a1622a8d9ef903f7975aafbef2453571bab`
- Built by: this repo's `renderer-unified.yml`, with the recipe of
  AngelAuraMC/amethyst-prebuilt-libraries@`ca883665dae3afeaba80b389d3d70f3ef96c9d82`
- License: MIT (`LICENSE-MIT.txt`)
- Copyright (c) 2016-2018 Sebastien Chevalier; Copyright (c) 2013-2016 Ryan Hileman;
  Copyright (c) 2025-2026 BZLZHH
- Bundled third-party code (pinned by that commit):
  - glslang, KhronosGroup/glslang@`7099c123729e02f81d70559e79ee4360096fdfe5`
    (`LICENSE-glslang.txt`)
  - SPIRV-Cross, KhronosGroup/SPIRV-Cross@`adec7acbf41a988713cdb85f93f26c8ca5ea863e`:
    Apache-2.0 (`LICENSE-Apache-2.0.txt`)

## `libEGL_angle.so`, `libGLESv2_angle.so`: ANGLE

- Project: ANGLE (Almost Native Graphics Layer Engine), AngelAuraMC's fork of google/angle
- Source: https://github.com/AngelAuraMC/angle/tree/e8e258c38c46114b20a86796d0f0f6084ddb1639
- Commit: `e8e258c38c46114b20a86796d0f0f6084ddb1639` (the binary reports
  `2.1.1 git hash: e8e258c38c46`), as pinned by
  AngelAuraMC/amethyst-prebuilt-libraries@`ca883665dae3afeaba80b389d3d70f3ef96c9d82`
- Built by: AngelAuraMC; added unmodified to `renderer-unified-v1`
- License: BSD-3-Clause (`LICENSE-BSD-3-Clause-ANGLE.txt`)
- Copyright 2018 The ANGLE Project Authors. ANGLE also builds in third-party code under
  permissive licenses; their notices are in `third_party/` at that commit.

## `libcutils.so`: AOSP libcutils (minimal)

- Project: Android Open Source Project, `system/core/libcutils` (`trace-dev.cpp` and
  `properties.cpp` only)
- Source: https://android.googlesource.com/platform/system/core/+/refs/tags/android-platform-13.0.0_r34/libcutils/
- Tag: `android-platform-13.0.0_r34`
- Built by: this repo's `renderer-unified.yml`, with AngelAuraMC/amethyst-prebuilt-libraries@`ca883665dae3afeaba80b389d3d70f3ef96c9d82`'s
  `build_libcutils.sh`
- License: Apache-2.0 (`LICENSE-Apache-2.0.txt`)
- Copyright (C) 2006, 2012 The Android Open Source Project

## `libglxshim.so`: GLXShim

- Project: GLXShim, a small `glXGetProcAddress` bridge used by the Zink (Kopper) renderer
- Source: https://github.com/Swung0x48/GLXShim/tree/39b93b5af6ffe1c278f33bbb3fb4436fca270843
- Commit: `39b93b5af6ffe1c278f33bbb3fb4436fca270843`
- Built by: this repo's `renderer-unified.yml`
- License: not declared by the author (licencia no declarada por el autor). The repository has
  no LICENSE file and no license statement. It's redistributed unmodified, as the rest of the
  Amethyst/PojavLauncher family does, with no objection known from its author.
- Copyright Swung0x48
