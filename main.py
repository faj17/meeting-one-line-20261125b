#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line entry: writes one sentence
to /output/entry.txt — the single line that could have replaced an entire
pointless meeting.

The line is built from two fragments: a SETUP that states the wasted hour,
and a PUNCH that turns it into the verdict — the meeting's only decision
is its own abolition. After this line, no one can justify holding the
meeting at all, ever again.
"""

import os

MAX_CHARS = 200

# Setup: the hour spent proving the meeting had no point.
SETUP = "We've spent an hour proving this meeting had no point"
# Punch: the twist — the only decision left is never to hold it again.
PUNCH = "so the only decision left is to never hold it again."


def assemble():
    """Join the fragments into the single entry line."""
    return f"{SETUP}, {PUNCH}"


def validate(text):
    """Gate: 1-200 chars of UTF-8 text, one line, one sentence,
    not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal period, no other sentence
    # terminators, and it must end the line.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if any(c in text for c in "!?;"):
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
