from typing import List
from unittest import TestCase


def maxSubArray(self, nums: List[int]) -> int:
    maximum = nums[0]
    sum = 0
    for num in nums:
        if sum < 0:
            sum = num
        else:
            sum += num
        maximum = max(maximum, sum)
    return maximum


class Test(TestCase):
    def test_max_sub_array(self):
        print(maxSubArray(self, [-2,1,-3,4,-1,2,1,-5,4]))
