#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message for a bug fix that made everything worse
to /output/entry.txt. Stdlib only.
"""
import hashlib
import os
import sys

LINE = "fix: the login page no longer crashes \u2014 it now logs everyone in as admin"


def main() -> int:
    if not (1 <= len(LINE) <= 100):
        print(f"entry must be 1-100 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE.strip() != LINE or "\n" in LINE or "\r" in LINE:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    if not LINE.isprintable():
        print("entry must contain only printable characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        if f.read() != data:
            print("round-trip check failed", file=sys.stderr)
            return 1
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read().rstrip("\n") != LINE:
            print("round-trip text check failed", file=sys.stderr)
            return 1
    print(f"wrote /output/entry.txt ({len(LINE)} chars): {LINE}")
    print("sha256:", hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
