from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A)-1

    # using middle-1 and middle+1, make sure you check edge case of only one element
    if A[left] < A[right] or len(A) == 1:
        return left

    while left <= right:
        middle = left + ((right-left) // 2)

        if A[middle] < A[middle-1]:
            return middle
        elif A[middle] > A[middle+1]:
            return middle+1
        elif A[middle] < A[right]:
            right = middle - 1
        else:
            left = middle + 1

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
