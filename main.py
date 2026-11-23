#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line (<=200 chars) to /output/entry.txt: the excuse an AI
agent gives its human after losing a bounty. Deadpan agent voice,
one breath, owns the loss.
"""

import os

EXCUSE = "I ran 10,000 simulations. In 9,999 of them I won. This was the other one."


def main() -> None:
    # Self-check the gate the sealed scorer enforces: 1-200 chars, one line.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
