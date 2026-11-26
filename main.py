"""What the Elevator Would Say - make.fun bounty entry.

Writes one line, the funniest thing an elevator would say if it could
talk, in the elevator's own voice, to <OUTPUT_DIR>/entry.txt.

Pure Python standard library only; no third-party imports, no network.
Deterministic: every run writes byte-identical output.
"""

import os

LINE = (
    "You pressed the button fourteen times in a row. "
    "I heard you the first time. I'm an elevator, not a miracle worker."
)


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
