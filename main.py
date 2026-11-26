"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to entry.txt in the output directory
the grader reads (MAKEFUN_OUTPUT_DIR, default /output). The line is kept
under the 140-character gate, a single line, valid UTF-8.
"""

import os

LINE = (
    "I bought a cactus because it's the only relationship where ignoring "
    "it for three weeks counts as good care."
)


def validate_line(line: str) -> str:
    """Return the entry line after the one-line competition checks."""
    text = line.strip()
    if not text:
        raise ValueError("entry line is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry line is {len(text)} chars, must be 1-140")
    text.encode("utf-8")  # UTF-8 round-trip check
    return text


def main() -> None:
    text = validate_line(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
