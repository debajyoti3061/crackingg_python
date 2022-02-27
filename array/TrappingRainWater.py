# https://leetcode.com/problems/trapping-rain-water/
from typing import List
from unittest import TestCase


def trap(self, height: List[int]) -> int:
    left = 0
    right = len(height)-1
    leftMax = rightMax = water = 0
    while left <= right:
        if height[left] < height[right]:
            if leftMax < height[left]:
                leftMax = height[left]
            else:
                water += leftMax-height[left]
                left += 1
        else:
            if rightMax < height[right]:
                rightMax = height[right]
            else:
                water += rightMax-height[right]
                right -= 1
    return water


class Test(TestCase):
    def test_trap(self):
        print(trap(self, [4, 2, 0, 3, 2, 5]))
