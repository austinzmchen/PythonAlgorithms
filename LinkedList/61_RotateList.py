# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr_head = head
        prev = None
        length = 0
        #
        while curr_head:
            length += 1
            prev = curr_head
            curr_head = curr_head.next
        #
        if length == 0 or k % length == 0:
            return head
        step = length - k % length - 1
        curr = head
        while step > 0:
            curr = curr.next
            step -= 1
        #
        new_head = curr.next
        curr.next = None
        prev.next = head
        return new_head