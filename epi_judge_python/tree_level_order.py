from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
        
    queue = deque()
    result = []
    queue.append(tree)

    while queue:
        level_length = len(queue)
        level_nodes = []

        for _ in range(level_length):
            node = queue.popleft()
            level_nodes.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
