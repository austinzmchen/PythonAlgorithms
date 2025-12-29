# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = False
        rHead = None
        
        while l1 or l2 or carry:    
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
                
            if carry:
                value += 1
                carry = False
                
            if value >= 10:
                carry = True
                value -= 10
                
            if not rHead:
                rHead = ListNode(value)  
                newHead = rHead
            else:
                rHead.next = ListNode(value)
                rHead = rHead.next
                
        return newHead
            
        