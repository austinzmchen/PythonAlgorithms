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

        mid = slow
        # reverse second half of the list
        head2 = reverse(mid)
        
        l1, l2 = head, head2
        while l1 is not mid: # incorrect: l1 is not l2:
            next = l1.next
            next2 = l2.next
            
            l1.next = l2
            l2.next = next
            
            l1 = next
            l2 = next2
            
        l1.next = None
        return head


def reverse(head):
    curr, prev = head, None
    while curr:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    return prev
