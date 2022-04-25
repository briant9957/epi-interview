from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    for x in range(len(A)):
        low = x
        high = len(A) - 1
        while low <= high:
            number = A[x] + A[low] + A[high]
            if number == t:
                return True
            elif number < t:
                low += 1
            else:
                high -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
