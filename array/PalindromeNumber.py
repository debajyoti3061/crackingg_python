from unittest import TestCase


def isPalindrome(n):
    original = n
    reverse = 0
    while n:
        reverse = reverse * 10 + n % 10
        n = int(n / 10)
    if original == reverse:
        return True
    else:
        return False


class Test(TestCase):
    def test_is_palindrome(self):
        print(isPalindrome(3543))
