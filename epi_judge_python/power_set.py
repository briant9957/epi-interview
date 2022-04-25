from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def generate(curr, input_set, result, idx):
        result.append(curr)

        for i in range(idx, len(input_set)):
            generate(curr + [input_set[i]], input_set, result, i+1)

    result = []
    generate([], input_set, result, 0)
    return result if input_set else [[]]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
