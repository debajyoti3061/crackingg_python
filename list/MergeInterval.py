from typing import List
from unittest import TestCase


def mergeInterval(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    result = []
    for interval in intervals:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            result.append([start, end])
            start = interval[0]
            end = interval[1]
    result.append([start, end])
    return result


class Test(TestCase):
    def test_merge_interval(self):
        print(mergeInterval(self, [[1, 3], [2, 6], [15, 18], [8, 10]]))
