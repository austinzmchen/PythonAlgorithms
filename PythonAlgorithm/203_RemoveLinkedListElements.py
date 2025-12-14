# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# add a fake previous node
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        fakeHead = ListNode(-1)
        fakeHead.next = head

        prev = fakeHead
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
            
        return fakeHead.next
        

# [1, 2, 2, 1]
# look for 2
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = head 
        iter = head
        before = None
        
        while iter:
            if iter.val == val:
                if newHead == iter:
                    iter = iter.next
                    newHead = iter
                    continue
                else:
                    before.next = iter.next
            
            if not before:
                before = newHead
            else:
                if iter.val != val: # need this so 2, 2, are not skipped
                    before = iter
                
            iter = iter.next
            
        return newHead
        