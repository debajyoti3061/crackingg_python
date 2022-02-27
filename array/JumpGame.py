from typing import List
from unittest import TestCase


def canJump(self, nums: List[int]) -> bool:
    maximum = 0
    for i in range(len(nums)):
        if maximum < i:
            return False
        maximum = max(i + nums[i], maximum)
    return True


class Test(TestCase):
    def test_can_jump(self):
        print(canJump(self, [2, 3, 1, 1, 4]))
