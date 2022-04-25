from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:

    def fill(row, column, visited):
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board[row][column] == 'B' or visited[row][column]:
            return

        visited[row][column] = True
        isEnclosed[row][column] = False

        fill(row+1, column, visited)
        fill(row-1, column, visited)
        fill(row, column+1, visited)
        fill(row, column-1, visited)

    isEnclosed = [[True for column in range(len(board[0]))] for row in range(len(board))]
    visited = [[False for column in range(len(board[0]))] for row in range(len(board))]

    for row in range(len(board)):
        fill(row, 0, visited)
        fill(row, len(board[0])-1, visited)

    for column in range(1, len(board[0])-1):
        fill(0, column, visited)
        fill(len(board)-1, column, visited)
    
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'W' and isEnclosed[row][column]:
                board[row][column] = 'B'

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
