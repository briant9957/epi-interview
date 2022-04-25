from test_framework import generic_test
import math

def square_root(k: int) -> int:
    start, end = 0, k
    while start <= end:
        middle = start + ((end-start) // 2)

        if middle**2 <= k and (middle+1)**2 > k:
            return middle
        elif middle**2 > k:
            end = middle-1
        else:
            start = middle+1

    return k


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
