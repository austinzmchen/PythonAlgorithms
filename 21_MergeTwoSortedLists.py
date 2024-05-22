class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(-1)
        newHead = temp
        
        while l1 != None or l2 != None:
            if not l1:
                newHead.next = l2
                l2 = l2.next
            elif not l2:
                newHead.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    newHead.next = l1
                    l1 = l1.next
                else:
                    newHead.next = l2
                    l2 = l2.next
                    
            newHead = newHead.next
                    
        return temp.next
                