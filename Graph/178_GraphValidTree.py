from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        adj_dict = {i:[] for i in range(n)}
        
        for e in edges:
            adj_dict[e[0]].append(e[1])
            adj_dict[e[1]].append(e[0])
        
        queue = [0]
        visited = [False] * n
        
        while queue:
            node = queue.pop(0)
            if visited[node]:
              return False
            visited[node] = True
            
            for adj in adj_dict[node]:
              if not visited[adj]:
                queue.append(adj)
        #
        for v in visited:
            if not v:
                return False
        #
        return True



print(Solution().valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]))
print(Solution().valid_tree(5, [[0,1],[1,2],[2,3],[1,3], [1,4]]))