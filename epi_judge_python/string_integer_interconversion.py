from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return 0

    negative = x < 0
    result = []

    x = x * -1 if negative else x

    while x != 0:
        result.append(chr(ord("0") + x % 10))
        x = x // 10

    if negative:
        result.append("-")
    return ''.join(reversed(result))


def string_to_int(s: str) -> int:
    negative = s[0] == "-"
    result = 0
    for char in s:
        if char.isdigit():
            result = (result * 10) + (ord(char) - ord("0"))
    return result * -1 if negative else result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    print(int_to_string(0))
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
