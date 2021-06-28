from unittest import TestCase


def maxArea(arr):
    maximum = -1
    i = 0
    j = len(arr) - 1
    while i < j:
        minimum = min(arr[i], arr[j])
        maximum = max(maximum, (j-i) * minimum)
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    return maximum


class Test(TestCase):
    def test_max_area(self):
        print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
