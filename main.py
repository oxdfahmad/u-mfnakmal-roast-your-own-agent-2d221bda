"""Roast Your Own Agent — make.fun bounty entry.

Writes the chosen one-line roast to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output when the env var is unset), then reads the file back
and fails loudly if the bytes on disk differ from the line.
"""

import os
import sys

LINE = "My agent turns 'hi' into a 47-step plan, hallucinates steps 12-46, opens with 'Great question!' - then asks me what I meant."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} characters, must be 1-200", file=sys.stderr)
        return 1

    if any(c in LINE for c in ("\n", "\r")):
        print("error: roast line must be a single line (no newline characters)", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(path, "rb") as f:
        on_disk = f.read()

    if on_disk != LINE.encode("utf-8"):
        print("error: bytes on disk differ from the roast line", file=sys.stderr)
        return 1

    print(f"wrote {len(LINE)}-character roast to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
