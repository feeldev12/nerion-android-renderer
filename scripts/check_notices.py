#!/usr/bin/env python3
"""Fails unless every shared library given (files or directories, searched recursively) is
named, as `libname.so`, in the notices file, and every license file the notices point to
(`LICENSE-*`) exists next to it. A renderer that ships without its notice would break the
license of that renderer.

usage: check_notices.py NOTICES.md PATH [PATH...]"""
import os
import re
import sys


def shared_libs(paths):
    for path in paths:
        if os.path.isdir(path):
            for root, _, names in os.walk(path):
                for name in names:
                    if name.endswith(".so"):
                        yield name
        elif path.endswith(".so"):
            yield os.path.basename(path)


def main(args):
    if len(args) < 2:
        print(__doc__)
        return 2
    notices, paths = args[0], args[1:]
    with open(notices, encoding="utf-8") as f:
        text = f.read()
    named = set(re.findall(r"`(lib[\w.+-]*\.so)`", text))
    libs = sorted(set(shared_libs(paths)))
    if not libs:
        print(f"::error::no .so files found in {paths}")
        return 1
    failed = 0
    for lib in libs:
        if lib not in named:
            print(f"::error::{lib} is not in {notices}")
            failed = 1
    here = os.path.dirname(os.path.abspath(notices))
    for ref in sorted(set(re.findall(r"`(LICENSE-[\w.+-]+)`", text))):
        if not os.path.isfile(os.path.join(here, ref)):
            print(f"::error::{notices} points to {ref}, which doesn't exist")
            failed = 1
    if not failed:
        print(f"{len(libs)} libraries, all with their notice in {notices}")
    return failed


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
