import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    len1 = 0
    curr = l0
    while curr:
        len1 += 1
        curr = curr.next

    len2 = 0
    curr = l1
    while curr:
        len2 += 1
        curr = curr.next
    
    if len2 > len1:
        len1, len2 = len2, len1
        l0, l1 = l1, l0

    while len1 > len2:
        l0 = l0.next
        len1 -= 1

    while l1 and l0:
        if l1 == l0:
            return l1
        l1 = l1.next
        l0 = l0.next

    return l1


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
