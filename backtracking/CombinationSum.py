from unittest import TestCase


def backTrack(output, tempList, nums, sum, position):
    if sum < 0:
        return
    elif sum == 0:
        output.append(tempList[:])
    else:
        for i in range(position, len(nums)):
            if i > position and nums[i] == nums[i - 1]:
                continue
            tempList.append(nums[i])
            backTrack(output, tempList, nums, sum - nums[i], i + 1)
            tempList.pop(len(tempList) - 1)


def combinationSum(self, nums, sum):
    output = []
    backTrack(output, [], nums, sum, 0)
    return output


class Test(TestCase):
    def test_combination_sum(self):
        print(combinationSum(self, [1, 3, 5, 1, 2], 5))
