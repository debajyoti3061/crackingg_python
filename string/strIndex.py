from unittest import TestCase


def strStr(self, haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1


class Test(TestCase):
    def test_str_str(self):
        print(strStr(self, 'hello', 'rllo'))
