# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy = ListNode(-1)
        even_dummy = ListNode(-1)
        odd_curr = odd_dummy
        even_curr = even_dummy
        #
        idx = 1
        while head:
            if idx % 2 == 1:
                odd_curr.next = head
                odd_curr = odd_curr.next
            else:
                even_curr.next = head
                even_curr = even_curr.next
            idx += 1
            head = head.next
        #
        odd_curr.next = even_dummy.next
        even_curr.next = None
        #
        return odd_dummy.next