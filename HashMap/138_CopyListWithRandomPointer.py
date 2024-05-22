class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
        
class Solution138:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = ListNode(-1)
        curr = head
        prev_new = dummy
        _dict = {}
        while curr:
            node = ListNode(curr.val)
            prev_new.next = node
            _dict[curr] = node
            #
            curr = curr.next
            prev_new = prev_new.next
        #
        curr_new = dummy.next
        curr = head
        while curr_new:
            curr_new.random = _dict[curr.random] if curr.random else None
            curr_new = curr_new.next
            curr = curr.next
        #
        return dummy.next