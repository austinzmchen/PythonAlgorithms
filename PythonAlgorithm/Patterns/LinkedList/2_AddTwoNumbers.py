# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from LinkedList import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)        
        curr = dummy_head
        
        carry = 0
        while l1 or l2 or carry:    
            v = 0
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next

            v += carry
            carry = v // 10
            v = v % 10

            curr.next = ListNode(v)
            curr = curr.next

        return dummy_head.next
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2:
            sum = 0
            if l1 and l2:
                sum = (l1.val + l2.val + carry)
                l1 = l1.next
                l2 = l2.next

            elif l1:
                sum = l1.val + carry
                l1 = l1.next

            elif l2:
                sum = l2.val + carry
                l2 = l2.next

            v = sum % 10
            carry = sum // 10
            curr.next = ListNode(v)
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)
            curr = curr.next

        return dummy.next