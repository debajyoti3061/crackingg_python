from unittest import TestCase
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        if nums[i] in hash_table:
            return [hash_table[nums[i]], i]
        else:
            hash_table[target - nums[i]] = i


def answer():
    result = twoSum([1, 2, 5, 7], 6)
    for p in result:
        print(p)


class Test(TestCase):
    def test_two_sum(self):
        answer()
