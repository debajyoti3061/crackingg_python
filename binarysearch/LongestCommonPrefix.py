from typing import List
from unittest import TestCase


def longestCommonPrefix(s: List[str]) -> str:
    min_length = len(min(s, key=len))
    low = 1
    high = min_length
    while low <= high:
        mid = (low + high) // 2
        if isCommonPrefix(s, mid):
            low = mid + 1
        else:
            high = mid - 1

    return s[0][:(low+high)//2]


def isCommonPrefix(s, length):
    prefix = s[0][:length]
    for i in s:
        if not i.startswith(prefix):
            return False
    return True


class Test(TestCase):
    def test_longest_common_prefix(self):
        print(longestCommonPrefix(['abcd', 'abcdef', 'abcee']))
