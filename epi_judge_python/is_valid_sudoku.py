from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    
    subArrays = [(0,0), (0,3), (0,6),
                 (3,0), (3,3), (3,6),
                 (6,0), (6,3), (6,6)]

    for startingPoint in subArrays:
        duplicates = set()
        for row in range(startingPoint[0], startingPoint[0]+3):
            for column in range(startingPoint[1], startingPoint[1]+3):
                if partial_assignment[row][column] != 0 and partial_assignment[row][column] not in duplicates:
                    duplicates.add(partial_assignment[row][column])
                elif partial_assignment[row][column] != 0 and partial_assignment[row][column] in duplicates:
                    return False

    for row in partial_assignment:
        duplicates = set()
        for element in row:
            if element != 0 and element not in duplicates:
                duplicates.add(element)
            elif element != 0 and element in duplicates:
                return False

    for x in range(len(partial_assignment[0])):
        duplicates = set()
        for y in range(len(partial_assignment)):
            if partial_assignment[y][x] != 0 and partial_assignment[y][x] not in duplicates:
                duplicates.add(partial_assignment[y][x])
            elif partial_assignment[y][x] != 0 and partial_assignment[y][x] in duplicates:
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
