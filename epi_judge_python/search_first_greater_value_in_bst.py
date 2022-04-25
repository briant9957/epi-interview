from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    return find_element(tree, k, None)

def find_element(node: BstNode , k, larger):
    if not node:
        return larger

    if node.data <= k :
        return find_element(node.right, k, larger)
    elif node.data > k:
        return find_element(node.left, k, node)

def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
