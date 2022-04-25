from test_framework import generic_test
import collections

def can_form_palindrome(s: str) -> bool:
    c = collections.Counter()
    for char in s:
        c.update({char: 1})
    
    allowance = 0 if len(s) % 2 == 0 else 1
    for key in c:
        if c[key] % 2 == 1:
            allowance -= 1
        if allowance < 0:
            return False
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
