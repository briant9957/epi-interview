from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return get_height(tree).balanced

def get_height(tree: BinaryTreeNode):
    BalancedAndHeight = collections.namedtuple("BalancedAndHeight", ["balanced", "height"])

    if not tree:
        return BalancedAndHeight(True, 0)
    
    leftTree = get_height(tree.left)
    if not leftTree.balanced:
        return BalancedAndHeight(False, -1)

    rightTree = get_height(tree.right)
    if not rightTree.balanced:
        return BalancedAndHeight(False, -1)

    return BalancedAndHeight((abs(leftTree.height - rightTree.height) <= 1), max(leftTree.height, rightTree.height) + 1)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
