from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        

class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        _map = {}
        q = [node]
        visited = {node}

        while q:
            n = q.pop(0)
            _map[n] = Node(n.val)
            for nb in n.neighbors:
                if nb not in visited:
                    q.append(nb)
                    visited.addnb

        q2 = [node]
        visited = {node}

        while q2:
            n = q2.pop(0)
            _map[n].neighbors.extend([_map[nb] for nb in n.neighbors])

            for nb in n.neighbors:
                if nb not in visited:
                    q2.append(nb)
                    visited.add(nb)

        return _map[node]
      

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        _dict = {}

        def recur(node):
            if not node:
                return None
            if cached_node := _dict.get(node.val):
                return cached_node
            
            curr = Node(node.val, [])
            _dict[curr.val] = curr

            for n in node.neighbors:
                nn = recur(n)
                curr.neighbors.append(nn)

            return curr
        return recur(node)
    
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
#
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
#
print(Solution().cloneGraph(node1))