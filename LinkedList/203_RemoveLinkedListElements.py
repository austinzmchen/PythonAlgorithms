# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# add a fake previous node
import sys
from typing import Optional
from LinkedList.ListNode import ListNode

class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(-sys.maxsize - 1)
        dummyHead.next = head

        curr = dummyHead.next
        prev = dummyHead

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return dummyHead.next

if __name__ == '__main__':
    pass
