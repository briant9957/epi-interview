from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []

    if not square_matrix:
        return result

    rowStart, rowEnd = 0, len(square_matrix[0])
    columnStart, columnEnd = 0, len(square_matrix)

    while abs(rowStart-rowEnd) > 1 and columnStart <= columnEnd:
        for i in range(columnStart, columnEnd):
            result.append(square_matrix[rowStart][i])
        for i in range(rowStart+1, rowEnd-1):
            result.append(square_matrix[i][columnEnd-1])
        for i in reversed(range(columnStart, columnEnd)):
            result.append(square_matrix[rowEnd-1][i])
        for i in reversed(range(rowStart+1, rowEnd-1)):
            result.append(square_matrix[i][columnStart])

        rowStart, rowEnd = rowStart + 1, rowEnd - 1
        columnStart, columnEnd = columnStart + 1, columnEnd - 1

    for i in range(columnStart, columnEnd):
        result.append(square_matrix[rowStart][i])

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
