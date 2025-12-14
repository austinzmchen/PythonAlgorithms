from LinkedList import ListNode


class Solution_86:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyNodeBefore = ListNode(-1)
        beforeCur = dummyNodeBefore
        dummyNodeAfter = ListNode(-1)
        afterCur = dummyNodeAfter
        
        while head != None:
            if head.val < x:
                beforeCur.next = head
                beforeCur = beforeCur.next
            else:
                afterCur.next = head
                afterCur = afterCur.next
            
            head = head.next
            
        beforeCur.next = dummyNodeAfter.next
        afterCur.next = None
        
        return dummyNodeBefore.next