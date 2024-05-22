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
        if not head: return None
        #
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        #
        if n > count:
            return None
        #
        dummy = ListNode(-1, head)
        curr = dummy
        i = 0
        while i < count - n:
            curr = curr.next
            i += 1
        #
        curr.next = curr.next.next
        return dummy.next