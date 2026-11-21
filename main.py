"""Writes a short text to relax the reader to /output/entry.txt."""

import os

TEXT = (
    "The light you are reading by left its star before the first city was "
    "built, and it will still be travelling long after every light below "
    "has gone out. It crossed all that dark only to arrive here, quietly, "
    "in your hands. Nothing in it hurries. Nothing ever has."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
