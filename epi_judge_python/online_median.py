from typing import Iterator, List

from test_framework import generic_test

import heapq

def online_median(sequence: Iterator[int]) -> List[float]:
    minHeap = []
    maxHeap = []

    result = []

    for i in sequence:
        heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, i))

        if (len(minHeap) + len(maxHeap)) % 2 == 0:
            result.append((minHeap[0] + (-1 * maxHeap[0])) / 2)
        else:
            result.append((-1* maxHeap[0]) / 1)

        if len(maxHeap) > len(minHeap):
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
