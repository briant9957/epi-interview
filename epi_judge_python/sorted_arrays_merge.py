from typing import List
import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result = []
    heap = []

    for array in sorted_arrays:
        heapq.heappush(heap, (array[0], 0, array))
    
    while heap:
        value, index, array = heapq.heappop(heap)
        result.append(value)
        if index+1 < len(array):
            heapq.heappush(heap, (array[index+1], index+1, array))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
