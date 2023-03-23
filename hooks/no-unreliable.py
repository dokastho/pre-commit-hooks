import argparse
import json
from typing import Any
from typing import Sequence


def raise_true_unreliable(f):
    lines = f.readlines()
    for line in lines:
        words = line.split()
        word: str
        for i, word in enumerate(words):
            if word.lower() == "unreliable":
                if (i + 1) != len(words):
                    nextword = words[i + 1]
                    if nextword.lower() == 'true':
                        raise ValueError('UNRELIABLE = true')


def main(argv) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, 'rb') as f:
            try:
                raise_true_unreliable(f)
            except ValueError as exc:
                print(f'{filename}: Unreliable set to true in ({exc})')
                retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())