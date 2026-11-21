#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is a fixed text: the demo went perfectly because the agent
did everything, including grading its own work. The program checks
the text fits the competition's 1-280 character window, then writes
it to /output/entry.txt as UTF-8.
"""

import os

JOKE = (
    "The demo worked perfectly: my AI agent wrote the code, "
    "ran the tests, and graded its own homework."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
