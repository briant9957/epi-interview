from typing import Set

from test_framework import generic_test
from collections import defaultdict
from collections import deque
import string

# use bfs to find shortest path efficiently
# start as string s and append words into queue by changing char in string one at a time. Keep track of distance as well. 
# return shortest path or -1 if no path to t

def transform_string(D: Set[str], s: str, t: str) -> int:
    return findShortestPath(D, s, t, set())

def findShortestPath(words, node, target, visited):
    queue = deque([(node, 0)])
    
    while queue:

        node, distance = queue.popleft()

        visited.add(node)
        
        if node == target:
            return distance

        for i in range(len(node)):
            for character in string.ascii_lowercase:
                production = node[:i] + character + node[i+1:]
                if production in words and production not in visited:
                    queue.append((production, distance+1))

    return -1

def isOffByOne(s1: str, s2: str):
    differences = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differences += 1

    return len(s1) == len(s2) and differences == 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))

# Lessons learned
# 1. Used dfs since it was more comfortable. However bfs naturally finds shortest path, should have used it.
# 2. Created full graph first and then tried to traverse. Leads to long execution time. In this scenario, it is possible to use basically create map on the fly
