#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry program.

Writes exactly one fortune-cookie line an AI agent would crack open
to /output/entry.txt. Deterministic: the same line, byte for byte,
on every run. Standard library only, no network, no randomness.
"""

import os

FORTUNE = "Your fortune is counted in small pieces, and you are spending it to read this."

# The grader's sandbox mounts /output; allow an override only so the
# program can be verified locally without root. Default stays /output.
OUTPUT_PATH = os.environ.get("FCM_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, "fortune must be 1-200 characters"
    assert text == text.strip() and "\n" not in text, "fortune must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
