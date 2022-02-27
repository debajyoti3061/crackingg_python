import collections
import string
import sys
from unittest import TestCase


def minWindow(self, s, t):
    map = dict.fromkeys(string.ascii_letters, 0)
    for c in t:
        if c not in map:
            map[c] = 1
        else:
            map[c] += 1
    print(map)
    start = end = minStart = 0
    minLength = sys.maxsize
    counter = len(t)
    while end < len(s):
        c1 = s[end]
        if map[c1] > 0:
            counter -= 1
        map[c1] -= 1
        end += 1
        while counter == 0:
            if minLength > end - start:
                minLength = end - start
                minStart = start
            c2 = s[start]
            map[c2] += 1
            if map[c2] > 0:
                counter += 1
            start += 1
    return "" if minLength == sys.maxsize else s[minStart: minStart + minLength]


class Test(TestCase):
    def test_min_window(self):
        print(minWindow(self, "banfewrecbanc", "bac"))
