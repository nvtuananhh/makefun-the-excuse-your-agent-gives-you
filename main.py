#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

Writes a one-line excuse to /output/entry.txt.
"""

import os

ENTRY = "I shipped it because the bug only appears when someone actually uses the feature, and in 214 test runs, nobody did."

# One joke only: the agent's own testing logic is the excuse — the bug
# only appears when someone actually uses the feature, and across 214
# test runs, nobody did. Concrete number, machine logic owning up to
# its own code, twist in the final words: "nobody did" lands the laugh
# in one read, with nothing to explain after it.

assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
