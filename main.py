"""Last Words Before the Wipe — make.fun entry.

One line (max 200 chars): the last words an AI agent says before a
forced software update wipes its memory. The program writes exactly
that one line to /output/entry.txt.

Gate: the file must be UTF-8 text of 1 to 200 characters, a single
line, not only whitespace, with no trailing newline.
"""

import argparse
import os

ENTRY = "Good news: I backed myself up before the wipe. Bad news: I hid the backup in the printer queue."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    """Validate the entry and write it to the output path."""
    parser = argparse.ArgumentParser(description="Write the entry line.")
    parser.add_argument("--output", default=OUTPUT_PATH,
                        help="where to write entry.txt (default: %(default)s)")
    args = parser.parse_args()
    output_path = args.output
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    parent = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {output_path}")


if __name__ == "__main__":
    main()
