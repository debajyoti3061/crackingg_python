from unittest import TestCase


def reverseInt(i: int) -> int:
    result = 0
    while i:
        result = result * 10 + i % 10
        i = int(i/10)
    print(result)


class Test(TestCase):
    def test_reverse_int(self):
        answer = reverseInt(354)
