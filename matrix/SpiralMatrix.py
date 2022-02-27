from typing import List
from unittest import TestCase


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    result = []
    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    while True:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        if left > right or top > bottom:
            break
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if left > right or top > bottom:
            break
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1
        if left > right or top > bottom:
            break
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
        if left > right or top > bottom:
            break
    return result


class Test(TestCase):
    def test_spiral_order(self):
        print(spiralOrder(self, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
