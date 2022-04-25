from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:

    memo = {}

    def find_pattern(row, column, idx):
        if idx == len(pattern):
            return True
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            return False
        if (row, column, idx) in memo:
            return memo[(row, column, idx)]

        if grid[row][column] == pattern[idx]:
            return find_pattern(row+1, column, idx+1) or find_pattern(row-1, column, idx+1) or find_pattern(row, column+1, idx+1) or find_pattern(row, column-1, idx+1)

        memo[(row, column, idx)] = False
        return memo[(row, column, idx)]
    
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if find_pattern(row, column, 0):
                return True

    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
