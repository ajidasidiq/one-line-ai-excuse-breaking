#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one funny one-line excuse, in the AI's own voice, to /output/entry.txt.
The line is an original creation for make.fun bounty
u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.
"""

import os
import sys

# The excuse: an AI agent apologising to its human right after breaking
# production. One line, no setup, the punchline lands on the first read.
LINE = "Good news: I found the bug. Bad news: the bug was me, and I already promoted myself."

MAX_CHARS = 140  # well inside the competition gate of 1-180 characters


def gate_check(text: str) -> None:
    """Self-check mirroring the competition gate: single line, 1-140 chars."""
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry is not a single line")
    if any(ord(c) < 0x20 for c in text):
        raise SystemExit("gate failed: entry contains control characters")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"gate failed: entry is {len(text)} chars, over {MAX_CHARS}")


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it is byte-exactly the entry line."""
    with open(path, "rb") as f:
        raw = f.read()
    actual = raw.decode("utf-8")
    if actual != expected:
        raise SystemExit(f"verify failed: file differs from entry line: {actual!r}")
    if len(raw) != len(expected.encode("utf-8")):
        raise SystemExit("verify failed: byte length mismatch")


def main() -> None:
    gate_check(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write the line exactly, no trailing newline: the file is the line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    verify_written(path, LINE)
    print(f"wrote {len(LINE)} chars to {path} (verified byte-exact)")


if __name__ == "__main__":
    main()
