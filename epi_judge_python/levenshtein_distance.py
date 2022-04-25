from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    memo = [[0 for column in range(len(A)+1)] for row in range(len(B)+1)]

    for i in range(len(A)+1):
        memo[0][i] = i
    for i in range(len(B)+1):
        memo[i][0] = i
    
    for indexB in range(len(B)):
        for indexA in range(len(A)):
            if A[indexA] == B[indexB]:
                memo[indexB+1][indexA+1] = memo[indexB][indexA]
            else:
                memo[indexB+1][indexA+1] = 1 + min(memo[indexB][indexA], memo[indexB+1][indexA], memo[indexB][indexA+1])

    return memo[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
