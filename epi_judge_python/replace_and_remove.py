import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    new_sequence = []

    for i in range(size):
        if s[i] == 'b':
            continue
        elif s[i] == 'a':
            new_sequence.append('d')
            new_sequence.append('d')
        else:
            new_sequence.append(s[i])

    for i in range(len(new_sequence)):
        s[i] = new_sequence[i]

    return len(new_sequence)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
