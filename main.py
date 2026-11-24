"""Write a single one-line office joke to the entry file.

The joke turns on the office buzzword "circle back": say it often
enough and the meeting itself becomes a roundabout.
"""

import os

# The entry is one line, assembled from a setup and a punchline.
SETUP = "I said 'circle back' so many times "
PUNCHLINE = "the meeting is now legally a roundabout."

ENTRY = SETUP + PUNCHLINE


def build_entry() -> str:
    """Return the entry line, checking it against the format gate."""
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be between 1 and 200 code points")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    return ENTRY


def main() -> None:
    """Write the entry line to entry.txt in the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(build_entry() + "\n")


if __name__ == "__main__":
    main()
