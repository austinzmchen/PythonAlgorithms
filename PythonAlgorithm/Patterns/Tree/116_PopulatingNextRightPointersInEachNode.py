from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        #
        q1 = deque()
        q1.append(root)
        #
        while len(q1) > 0:
            prev = None
            size = len(q1)
            for i in range(0, size):
                curr = q1.popleft()
                #
                if curr.left: q1.append(curr.left)
                if curr.right: q1.append(curr.right)
                #
                if prev:
                    prev.next = curr
                prev = curr
            #
            prev.next = None
        #
        return root