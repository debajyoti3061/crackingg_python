from typing import List
from unittest import TestCase


def isValidSudoku(self, board: List[List[str]]) -> bool:
    seen = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '.':
                if board[i][j] + 'in row' + str(i) in seen \
                        or board[i][j] + 'in column' + str(j) in seen \
                        or board[i][j] + 'in box' + str(i // 3) + str(j // 3) in seen:
                    return False
                else:
                    seen.add(board[i][j] + 'in row' + str(i))
                    seen.add(board[i][j] + 'in column' + str(j))
                    seen.add(board[i][j] + 'in box' + str(i // 3) + str(j // 3))
    return True


class Test(TestCase):
    def test_is_valid_sudoku(self):
        print(isValidSudoku(self, [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
