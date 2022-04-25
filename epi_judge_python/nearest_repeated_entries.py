from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    closest = len(paragraph)
    distances = {}

    for i in range(len(paragraph)):
        if paragraph[i] in distances:
            closest = min(closest, i - distances[paragraph[i]])
        distances[paragraph[i]] = i

    # remember to check if any duplicate words are found, if not return -1
    return closest if closest < len(paragraph) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
