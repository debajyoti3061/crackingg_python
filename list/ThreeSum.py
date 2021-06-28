from unittest import TestCase


# https://leetcode.com/problems/3sum/
def threesum(nums):
    result = list()
    nums.sort()
    for i in range(0, len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif sum > 0:
                k -= 1
            else:
                j += 1
    return result


class Test(TestCase):
    def test_threesum(self):
        print(threesum([-1, 0, 1, 2, -1, -4]))
