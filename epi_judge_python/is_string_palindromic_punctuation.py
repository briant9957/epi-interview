from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    start, end = 0, len(s) - 1

    while start <=  end:
        while start < len(s)-1  and not s[start].isalnum():
            start += 1
        while end > 0 and not s[end].isalnum():
            end -= 1
        
        if s[start].isalnum() and s[end].isalnum() and s[start].lower() != s[end].lower():
            return False
        
        start += 1
        end -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
