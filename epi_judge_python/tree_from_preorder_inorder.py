from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    def construct(preorder, inorder):
        if not inorder:
            return None

        node = BinaryTreeNode(preorder.pop(0))

        indexOfNode = inorder.index(node.data)

        node.left = construct(preorder, inorder[:indexOfNode])
        node.right = construct(preorder, inorder[indexOfNode+1:])

        return node

    return construct(preorder, inorder)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
