from typing import Iterator, List
import heapq

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = []
    result = []

    for num in sequence:
        heapq.heappush(heap, num)
        if len(heap) > k:
            result.append(heapq.heappop(heap))

    while heap:
        result.append(heapq.heappop(heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
