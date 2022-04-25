from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    memo = [0] * (final_score + 1)
    memo[0] = 1

    for play_score in individual_play_scores:
        for i in range(1, final_score+1):
            if i - play_score >= 0:
                memo[i] += memo[i-play_score]   
    return memo[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
