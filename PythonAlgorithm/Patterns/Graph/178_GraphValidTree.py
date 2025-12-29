# Problem Description
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# What Makes a Valid Tree?
# A valid tree must satisfy two conditions:

# No cycles - There should be no circular paths
# All nodes connected - The graph must be fully connected (one connected component)

# Example 1
# n = 5
# edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: True
# Graph looks like:
#     0
#    /|\
#   1 2 3
#   |
#   4

# Example 2
# n = 5
# edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: False
# Has a cycle: 1-2-3-1

# Example 3
# n = 5
# edges = [[0,1], [0,2]]
# Output: False
# Not fully connected (nodes 3 and 4 are isolated)


from typing import List

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree1(self, n: int, edges: List[List[int]]) -> bool:
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

        for v in visited:
            if not v:
                return False

        return True

    
    # traditional approach
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        in_degs = {}
        adj_dict = {}
        
        for i in range(n):
            in_degs[i] = 0
            
        for e in edges:
            n1, n2 = e
            
            in_degs[n1] = in_degs.get(n1, 0) + 1
            in_degs[n2] = in_degs.get(n2, 0) + 1
            
            adj_dict.setdefault(n1, [])
            adj_dict[n1].append(n2)
            
            adj_dict.setdefault(n2, [])
            adj_dict[n2].append(n1)
        
        queue = []
        visited = set()
        
        for i, v in in_degs.items():
            if v == 1:
                queue.append(i)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                
                visited.add(node)
                in_degs[node] -= 1
                
                for adj in adj_dict.get(node, []):
                    in_degs[adj] -= 1
                    if in_degs.get(adj) == 1:
                        queue.append(adj)

        return len(visited) == n


print(Solution().valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]))
print(Solution().valid_tree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))
print(Solution().valid_tree(5, [[0,1],[0,2]]))