class Solution:
    
    # Nodes with degree 1 cannot be inside a cycle (a cycle needs every node to have degree ≥ 2).
    # So we push all degree-1 nodes into a queue and remove them.
    # When we remove a node, its neighbor's degree decreases; that neighbor might become a new leaf (degree 1), so we remove it next.
    # After this process finishes, the only nodes left with degree > 0 are exactly the cycle nodes.
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import deque
        n = len(edges)
        
        in_degs = {}
        adj_dict = {}
        
        for frm, to in edges:
            in_degs[frm] = in_degs.get(frm, 0) + 1
            in_degs[to] = in_degs.get(to, 0) + 1
            
            adj_dict.setdefault(frm, [])
            adj_dict[frm].append(to)
            
            adj_dict.setdefault(to, [])
            adj_dict[to].append(frm)

        # if you use the in_degs, you don't need a visited set to track
        q = deque()
        
        for i in range(1, n + 1): # value start from 1
            if in_degs[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            in_degs[node] -= 1
            
            for nb in adj_dict.get(node, []):
                in_degs[nb] -= 1
                if in_degs[nb] == 1:
                    q.append(nb)

        for frm, to in reversed(edges):
            if in_degs[frm] == 2 and in_degs[to] == 2:
                return [frm, to]
        return []
    
    
print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]]))