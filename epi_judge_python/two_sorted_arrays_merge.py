from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:

    back = m + n - 1
    first, second = m-1, n-1
    while first >= 0 and second >= 0:
        if A[first] >= B[second]:
            A[back] = A[first]
            first -= 1
        else:
            A[back] = B[second]
            second -= 1
        back -= 1

    while first >= 0:
        A[back] = A[first]
        back, first = back - 1, first - 1
    
    while second >= 0:
        A[back] = B[second]
        back, second = back - 1, second - 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
