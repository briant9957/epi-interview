from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def recurse(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.data != node2.data:
            return False

        return recurse(node1.right, node2.left) and recurse(node1.left, node2.right)

    return recurse(tree.left, tree.right) if tree else True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
