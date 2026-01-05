# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, dummy
        i = 0

        while r:
            if i == k:
                next = r.next
                old_start = l.next
                new_start, new_end = reverse(l.next, r)

                l.next = new_start
                new_end.next = next # l.next is the old head

                l, r = new_end, new_end
                i = 0

            i += 1
            r = r.next

        return dummy.next


def reverse(start, end):
    prev, curr = None, start
    end_next = end.next

    while curr is not end_next:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next
    
    return end, start