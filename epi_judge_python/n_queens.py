from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def n_queens_helper(row):
        if row == n:
            result.append(columns.copy())
        for i in range(n):
            if not any(abs(i-c) in (0, abs(row-r)) for r, c in enumerate(columns[:row])):
                columns[row] = i
                n_queens_helper(row+1)

    
    result = []
    columns = [0] * n
    n_queens_helper(0)
    return result



def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
