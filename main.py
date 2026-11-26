#!/usr/bin/env python3
"""Pigeon Pitch, One Line entry: a single line, at most 200 characters.

The program writes one elevator pitch to /output/entry.txt — a city
pigeon pitching investors on its crumb-delivery startup, in the
pigeon's own voice: lunch on your ledge before you even know you're
hungry, seed round open, worms accepted as payment. One line, one
sentence, nothing more. The entry is checked before writing: a
single line, one sentence, within the character cap.
"""

import os

SENTENCE = (
    "We turn dropped crumbs into subscriptions: PigeonPost delivers "
    "lunch to your ledge before you even know you're hungry — seed "
    "round open, worms accepted as payment."
)


def main():
    text = SENTENCE.strip()
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} is outside 1..200 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
