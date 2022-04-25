from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    
    if not L or not L.next or start == finish:
        return L

    i = start-1
    current = L
    dummyHead = before = ListNode(0)
    dummyHead.next = L
    while i > 0:
        before = current
        current = current.next
        i -= 1
    
    tail = current
    head = current

    for _ in range(start, finish+1):
        nextNode = current.next
        current.next = head
        head = current
        current = nextNode
    
    before.next = head
    tail.next = current
    
    return dummyHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
