import sys
import argparse
from alphabet_soup.core import load_puzzle, find_word

VERSION = "1.0.0"  # You can update this as needed

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Solve a word-search puzzle and output answer key."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"alphabet-soup {VERSION}",
        help="Show program's version number and exit"
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        help="Path to the puzzle text file"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.input_file:
        print("Error: input_file argument is required.", file=sys.stderr)
        sys.exit(1)

    grid, words = load_puzzle(args.input_file)

    for word in words:
        pos = find_word(grid, word)
        if pos:
            (start, end) = pos
            print(f"{word} {start[0]}:{start[1]} {end[0]}:{end[1]}")
        else:
            print(f"{word} not found")


if __name__ == "__main__":
    main()
