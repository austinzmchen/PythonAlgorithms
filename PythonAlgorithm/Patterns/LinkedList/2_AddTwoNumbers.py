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
        