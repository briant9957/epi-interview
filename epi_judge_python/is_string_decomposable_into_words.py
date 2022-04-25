import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    def decompose(start, result, memo):
        if start == len(domain):
            return True
        if not memo[start]:
            return False

        for idx in range(start, len(domain)):
            if domain[start:idx+1] in dictionary:
                result.append(domain[start:idx+1])
                if decompose(idx+1, result, memo):
                    return True
                result.pop()

        memo[start] = False
        return memo[start]
    
    memo = [True] * len(domain)
    result = []
    isDecomposable = decompose(0, result, memo)
    return result if isDecomposable else []

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
