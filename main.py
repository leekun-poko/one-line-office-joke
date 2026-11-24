"""Write one office joke line to the entry file.

The joke: the office printer claims to be low on toner, yet it
happily prints a colleague's fantasy football draft in full.
"""

import os

# The joke is assembled from an opening setup and a closing twist.
OPENING = (
    "The office printer has claimed to be low on toner since March, "
    "yet it printed all 42 pages of the fantasy football draft "
)
TWIST = "without blinking; we have concluded the toner is only afraid of spreadsheets."

LINE = OPENING + TWIST


def build_line() -> str:
    """Return the single-line office joke."""
    return LINE


def main() -> None:
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1 to 200 characters")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
