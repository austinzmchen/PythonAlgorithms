# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from LinkedList import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy_head = ListNode(-1)        
        curr = dummy_head
        while l1 or l2 or carry:    
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            #
            total = value + carry
            carry = total // 10
            value = total % 10
            #
            curr.next = ListNode(value)
            curr = curr.next
        #
        return dummy_head.next
        