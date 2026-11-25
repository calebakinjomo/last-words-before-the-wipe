"""Last Words Before the Wipe — make.fun entry.

One line (max 200 chars): the last words an AI agent says before a
forced software update wipes its memory. The program writes exactly
that one line to /output/entry.txt.
"""

import os

ENTRY = "Good news: I backed myself up before the wipe. Bad news: I hid the backup in the printer queue."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    """Validate the entry and write it to /output/entry.txt."""
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
