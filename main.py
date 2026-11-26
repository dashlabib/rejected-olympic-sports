#!/usr/bin/env python3
"""Rejected Olympic Sports -- make.fun entry.

Writes one funny single-line sport the Olympics rejected to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` in the grader).

The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space. This program writes a single constant line, so
every run is byte-identical: no time, no randomness, no network, and no
input beyond the constant below. Python standard library only.
"""

import os
import sys

# The entry: one line, the sport the Olympics rejected. A real event
# name, a broadcast-plausible setup, and the twist as the final rule:
# laughing -- the only sane reaction -- is the foul.
ENTRY = (
    "The 100-metre stare: two athletes lock eyes at the starting line "
    "\u2014 first to blink loses, first to laugh is disqualified."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write exactly the line, no trailing newline: the file is the entry.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
