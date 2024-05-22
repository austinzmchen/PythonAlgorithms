class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        iter = head
        
        i = 0
        while i < n:
            if not iter:
                return head
            iter = iter.next
            i += 1
            
        if not iter:
            return head.next
        
        before = head
        while iter:
            if not iter.next:
                before.next = before.next.next
                return head
            before = before.next
            iter = iter.next
            
        return head