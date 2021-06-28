from unittest import TestCase


def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    a = set()
    i = j = 0
    while i < n and j < n:
        if s[j] not in a:
            a.add(s[j])
            ans = max(ans, j-i+1)
            j += 1
        else:
            a.remove(s[i])
            i += 1
    print(ans)




class Test(TestCase):
    def test_length_of_longest_substring(self):
        lengthOfLongestSubstring("gfdliofdsl")