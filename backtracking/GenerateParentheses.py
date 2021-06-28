from unittest import TestCase


def backtrack(list, str, open, close, max):
    if len(str) == max * 2:
        list.append(str)
        return
    if open < max:
        backtrack(list, str + "(", open + 1, close, max)
    if close < open:
        backtrack(list, str + ")", open, close + 1, max)
    return list


def generateParenthesis(n):
    a = []
    output = backtrack(a, "", 0, 0, n)
    print(' '.join(output))


class Test(TestCase):
    def test_generate_parenthesis(self):
        generateParenthesis(3)
