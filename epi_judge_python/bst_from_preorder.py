from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    def rebuild(preorder, upper):
        if not preorder:
            return None

        node = BstNode(preorder[0])
        preorder.pop(0) 
        
        if preorder and preorder[0] < node.data:
            node.left = rebuild(preorder, node.data)
        if preorder and node.data < preorder[0] < upper:
            node.right = rebuild(preorder, upper)

        return node

    return rebuild(preorder_sequence, float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
