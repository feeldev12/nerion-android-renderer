#!/usr/bin/env python3
"""Fails unless every ELF shared object given (files or directories) has all of its LOAD
segments aligned to at least 16 KB. Google Play rejects arm64 bundles otherwise
("Tu app no admite tamaños de página de 16 KB"), and Android 15+ devices with 16 KB pages
can't load them."""
import os
import struct
import sys

MIN_ALIGN = 16384


def load_aligns(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:4] != b"\x7fELF" or data[4] != 2:  # 64-bit only: the bundle is arm64-v8a
        return None
    phoff = struct.unpack_from("<Q", data, 0x20)[0]
    phentsize, phnum = struct.unpack_from("<HH", data, 0x36)
    aligns = []
    for i in range(phnum):
        off = phoff + i * phentsize
        if struct.unpack_from("<I", data, off)[0] == 1:  # PT_LOAD
            aligns.append(struct.unpack_from("<Q", data, off + 48)[0])
    return aligns


def main(args):
    files = []
    for arg in args:
        if os.path.isdir(arg):
            files += [os.path.join(root, n) for root, _, names in os.walk(arg) for n in names if n.endswith(".so")]
        else:
            files.append(arg)
    if not files:
        print("::error::no .so files to check")
        return 1
    bad = 0
    for path in sorted(files):
        aligns = load_aligns(path)
        if aligns is None:
            print(f"::error::{path} is not a 64-bit ELF")
            bad += 1
            continue
        lowest = min(aligns)
        status = "ok" if lowest >= MIN_ALIGN else "TOO SMALL"
        print(f"{lowest:>6}  {status:9}  {path}")
        if lowest < MIN_ALIGN:
            print(f"::error::{path} has a LOAD segment aligned to {lowest} bytes (needs {MIN_ALIGN})")
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
