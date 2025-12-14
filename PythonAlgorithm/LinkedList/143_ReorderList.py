# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        #
        mid = slow
        # reverse second half of the list
        prev = None
        while slow is not None:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        #
        last = prev
        #
        l, r = head, last
        while l is not mid:
            l_next = l.next
            r_next = r.next
            l.next = r
            r.next = l_next
            l = l_next
            r = r_next
        l.next = None
        #
        return head
        