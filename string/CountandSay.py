from unittest import TestCase


def getOutput(input) -> str:
    character = input[0]
    count = 1
    output = str()
    for i in range(1, len(input)):
        if input[i] == character:
            count += 1
        else:
            output += str(count)
            output += character
            character = input[i]
            count = 1
    output += str(count)
    output += character
    return output


def countAndSay(n) -> str:
    output = '1'
    for i in range(1, n):
        output = getOutput(output)
    return output


class Test(TestCase):
    def test_count_and_say(self):
        print(countAndSay(5))
