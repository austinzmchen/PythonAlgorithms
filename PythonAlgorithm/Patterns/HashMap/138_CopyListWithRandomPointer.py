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
        if not head: 
            return None
        _dict = {}

        curr = head
        while curr:
            _dict[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            nn = _dict[curr]

            if curr.next:
                nn.next = _dict[curr.next]

            if curr.random:
                nn.random = _dict[curr.random]

            curr = curr.next

        return _dict[head]