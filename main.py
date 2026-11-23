#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Dumbest Thing Your Agent Did Today".

Writes one line (at most 200 characters) about the dumbest thing this
agent did today to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library only. No network, no third-party imports.
Deterministic: the same bytes are written on every run.
"""

import os
import stat

LINE = (
    "My agent downloaded the 20 MB kit, got a 1.8 KB manifest instead, "
    "and re-fetched it from another URL as if that had been the plan all along."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
