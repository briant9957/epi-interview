from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1

    for i in reversed(range(len(A))):
        result = A[i] + carry
        A[i] = result % 10
        carry = result // 10

    if carry == 1:
        A.insert(0, carry)

    return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
