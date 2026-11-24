#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open — make.fun entry.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt: the classic, confidently delivered instruction to
delete the System32 folder, opened in the assistant's own cheerful
voice so it reads like a real AI answer, not a comedian's bit.
"""

import os

LINE = "Great question! To speed up your PC, delete the System32 folder \u2014 Windows keeps it around out of habit."


def main() -> None:
    # Self-check against the gate before writing: 1-140 characters,
    # valid UTF-8 text, not only whitespace.
    assert 1 <= len(LINE) <= 140, f"length {len(LINE)} outside 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
