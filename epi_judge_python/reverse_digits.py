from test_framework import generic_test


def reverse(x: int) -> int:
    negative = x < 0

    positiveX = abs(x)
    reversedX = 0

    while positiveX != 0:
        digit = positiveX % 10
        positiveX = positiveX // 10

        reversedX = (reversedX * 10) + digit
    
    return reversedX if not negative else -1 * reversedX

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
