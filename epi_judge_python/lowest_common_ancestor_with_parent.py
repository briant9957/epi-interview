import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not node0 or not node1:
        return None
        
    node0Distance = getDistanceFromRoot(node0)
    node1Distance = getDistanceFromRoot(node1)

    if node0Distance < node1Distance:
        node1 = moveUpToRoot(node1, node1Distance - node0Distance)
    else:
        node0 = moveUpToRoot(node0, node0Distance - node1Distance)

    parent = findSameParent(node0, node1)
    return parent

def getDistanceFromRoot(node):
    if node.parent is None:
        return 1
    return 1 + getDistanceFromRoot(node.parent)

def moveUpToRoot(node, distance):
    if distance == 0:
        return node
    
    return moveUpToRoot(node.parent, distance-1)

def findSameParent(node0: BinaryTreeNode, node1: BinaryTreeNode):
    if node0 is None or node1 is None:
        return None
    if node0 == node1:
        return node0

    return findSameParent(node0.parent, node1.parent)

@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
