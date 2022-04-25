from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    idx1 = idx2 = 0
    len1, len2 = len(A), len(B)
    result = []

    while idx1 < len1 and idx2 < len2:
        if A[idx1] == B[idx2] and (not result or result[-1] != A[idx1]):
            result.append(A[idx1])
            idx1, idx2 = idx1 + 1, idx2 + 1
        elif A[idx1] < B[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
