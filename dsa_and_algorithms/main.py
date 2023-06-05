"""
Data Structures and Algorithms - my answers in Python
"""

import sys
from importlib import metadata

from natsort import natsorted


def main():
    # pylint: disable=missing-function-docstring
    names = sys.argv[1:]
    days = metadata.entry_points().select(group="dsa_and_algorithms.days")
    for entry in natsorted(days, key=lambda entry: entry.name):
        # day = "".join(c for c in entry.name if c.isdigit())
        if names and entry.name.removeprefix("day") not in names:
            continue
        print(f"Day {entry.name.removeprefix('day')}")
        for main_func in entry.load():
            print(main_func())
        print()


if __name__ == "__main__":
    main()
