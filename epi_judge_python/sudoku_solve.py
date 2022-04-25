import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def is_valid(x, y, partial_assignment):
       row = [partial_assignment[y][column] for column in range(len(partial_assignment[0])) if partial_assignment[y][column] != 0]
       column = [partial_assignment[row][x] for row in range(len(partial_assignment)) if partial_assignment[row][x] != 0]

       rowRegion = (y // 3) * 3
       columnRegion = (x // 3) * 3

       region = [partial_assignment[row][column] for row in range(rowRegion, rowRegion+3) for column in range(columnRegion, columnRegion+3) if partial_assignment[row][column] != 0]
       return not has_duplicate(row) and not has_duplicate(column) and not has_duplicate(region)
    
    def fill(x, y, partial_assignment):
        if x == len(partial_assignment[0]):
            x = 0
            y += 1
            if y == len(partial_assignment):
                return True

        if partial_assignment[y][x] != 0:
            return fill(x+1, y, partial_assignment)

        for i in range(1, len(partial_assignment)+1):
            partial_assignment[y][x] = i
            if is_valid(x, y, partial_assignment):
                if (fill(x+1, y, partial_assignment)):
                    return True
        partial_assignment[y][x] = 0

        return False

    return fill(0, 0, partial_assignment)



def has_duplicate(a):
    numbers = set()
    for i in a:
        if i in numbers:
            return True
        else:
            numbers.add(i)

    return False

def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
