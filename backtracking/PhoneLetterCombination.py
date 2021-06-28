from unittest import TestCase

mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
output = []


def letterCombinations(combination, digits):
    if len(digits) == 0:
        output.append(combination)
    else:
        digit = digits[0:1]
        letters = mapping[digit]
        for i in range(len(letters)):
            letter = mapping[digit][i: i + 1]
            letterCombinations(combination + letter, digits[1:])


class Test(TestCase):
    def test_letter_combinations(self):
        letterCombinations('', '23')
        print(output)
