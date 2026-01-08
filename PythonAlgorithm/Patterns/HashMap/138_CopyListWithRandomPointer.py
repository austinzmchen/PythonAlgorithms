class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
        
class Solution138:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        
        prev_new = dummy
        _dict = {}
        
        curr = head
        while curr:
            node = Node(curr.val)
            prev_new.next = node
            _dict[curr] = node

            curr = curr.next
            prev_new = prev_new.next

        curr_new = dummy.next
        
        curr = head
        while curr_new:
            curr_new.random = _dict[curr.random] if curr.random else None
            curr_new = curr_new.next
            curr = curr.next

        return dummy.next
    
    
    # use Node as dict key
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        _dict = {}

        curr2 = head
        while curr2:
            _dict[curr2] = Node(curr2.val)
            curr2 = curr2.next

        curr2 = head
        while curr2:
            curr = _dict[curr2]
            if dummy.next is None:
                dummy.next = curr

            if curr2.next:
                curr.next = _dict[curr2.next]

            if curr2.random:
                curr.random = _dict[curr2.random]

            curr2 = curr2.next

        return dummy.next