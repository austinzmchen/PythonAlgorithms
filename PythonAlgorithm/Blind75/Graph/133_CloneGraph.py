
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        

class Solution:
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
    
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        edges = {}

        def recur(n):
            if not n:
                return

            if n.val in edges:
                return

            for nb in n.neighbors:
                edges.setdefault(n.val, set())
                edges[n.val].add(nb.val)
                recur(nb)
        recur(node)

        node_dict = {}
        for v in edges.keys():
            node_dict[v] = Node(v, [])

        for v, _set in edges.items():
            for nb_val in _set:
                nb = node_dict[nb_val]
                node_dict[v].neighbors.append(nb)

        return node_dict[node.val]
    
    
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        node_dict = {}

        def recur(node):
            if not node:
                return None
            if n := node_dict.get(node.val):
                return n
            
            new_node = Node(node.val, [])
            node_dict[node.val] = new_node

            for nb in node.neighbors:
                new_nb = recur(nb)
                new_node.neighbors.append(new_nb)

            return new_node
        
        return recur(root)
    
    
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