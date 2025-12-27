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
        
        curr, curr2 = head, head2
        while curr is not mid:
            next = curr.next
            next2 = curr2.next
            
            curr.next = curr2
            curr2.next = next
            
            curr = next
            curr2 = next2
            
        curr.next = None
        return head


def reverse(head):
    curr, prev = head, None
    while curr:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    return prev
