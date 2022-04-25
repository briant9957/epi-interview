from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if not L1 or not L2:
        return L1 or L2
    
    dummy = ListNode(0)
    head = dummy
    while L1 and L2:
        if L1.data <= L2.data:
            dummy.next = L1
            dummy, L1 = dummy.next, L1.next
        else:
            dummy.next = L2
            dummy, L2 = dummy.next, L2.next
    
    if L1 or L2:
        dummy.next = L1 or L2

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
