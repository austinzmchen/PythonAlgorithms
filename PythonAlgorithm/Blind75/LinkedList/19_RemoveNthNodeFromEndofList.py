from LinkedList import ListNode

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
      
      
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        if n > size:
            return None
        
        m = size - n
        i = 0
        prev, curr = dummy, head

        while i < m:
            prev = curr
            curr = curr.next
            i += 1

        # remove the curr node
        prev.next = curr.next
        return dummy.next