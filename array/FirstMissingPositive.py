from typing import List
from unittest import TestCase


def firstMissingPositive(self, nums: List[int]) -> int:
    # ignore nums <= 0 or > size
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = len(nums) + 1
    # iterate and change index to negative
    for i in range(len(nums)):
        num = abs(nums[i])
        if num > len(nums):
            continue
        num -= 1
        if nums[num] > 0:
            nums[num] = -1 * nums[num]
    # find 1st non negative index
    for i in range(len(nums)):
        if nums[i] > 0:
            return i+1
    return 0


class Test(TestCase):
    def test_first_missing_positive(self):
        print(firstMissingPositive(self, [3, 4, -1, 1]))
