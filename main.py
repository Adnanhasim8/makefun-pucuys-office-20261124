"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt.
Python 3.13 standard library only; no network at run time.
"""

import os

JOKE = "IT closed my ticket as \"resolved\" \u2014 the real problem, it turns out, was that I noticed it."


def main() -> None:
    # Gate assertions: one line, 1-200 chars, non-empty, no trailing newline.
    assert JOKE, "entry must not be empty"
    assert JOKE.strip() == JOKE, "entry must not have leading/trailing whitespace"
    assert "\n" not in JOKE and "\r" not in JOKE, "entry must be a single line"
    assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
