from typing import List
from unittest import TestCase


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    map = dict()
    for str in strs:
        sortedStr = ''.join(sorted(str))
        if sortedStr not in map:
            map[sortedStr] = []

        map[sortedStr].append(str)
    return map.values()


class Test(TestCase):
    def test_group_anagrams(self):
        print(groupAnagrams(self, ["eat","tea","tan","ate","nat","bat"]))
