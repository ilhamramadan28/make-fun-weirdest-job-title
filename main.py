"""Write the weirdest job title to /output/entry.txt.

Gate: the entry must be one line, UTF-8, 1-60 characters, not
whitespace-only. The output file is written world-readable (0644)
so the grader can read it.
"""

import os
import sys


def main() -> int:
    entry_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 60:
        print("entry is longer than 60 characters", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry contains control characters", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
