from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_binary_tree_bst_helper(tree, float("-inf"), float("inf"))

def is_binary_tree_bst_helper(tree, minBoundary, maxBoundary):
    if not tree:
        return True
    
    if minBoundary <= tree.data <= maxBoundary:
        return is_binary_tree_bst_helper(tree.left, minBoundary, tree.data) and is_binary_tree_bst_helper(tree.right, tree.data, maxBoundary)
    
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
