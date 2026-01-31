# 323. Number of Connected Components in an Undirected Graph
# Problem Description
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (where each edge is a pair of nodes), write a function to find the number of connected components in the graph.
# A connected component is a group of nodes where you can reach any node from any other node in that group through the edges.

# Example 1
# n = 5
# edges = [[0,1], [1,2], [3,4]]
# Output: 2
# Component 1: {0, 1, 2}
# Component 2: {3, 4}
#
# Visual:
# 0---1---2    3---4

# Example 2
# n = 5
# edges = [[0,1], [1,2], [2,3], [3,4]]
# Output: 1
# All nodes connected in one component
#
# Visual:
# 0---1---2---3---4

# Example 3
# n = 4
# edges = []
# Output: 4
# Each node is its own component: {0}, {1}, {2}, {3}

# Example 4
# n = 6
# edges = [[0,1], [1,2], [3,4]]
# Output: 3
# Component 1: {0, 1, 2}
# Component 2: {3, 4}
# Component 3: {5}


class Solution323:
  
    def countComponents(self, n: int, edges: list) -> int:
        adj_dict = {i: [] for i in range(n)}
        
        for e in edges:
            adj_dict[e[0]].append(e[1])
            adj_dict[e[1]].append(e[0])
        
        count = 0
        visited = set()
        
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
        
        for adj in adj_dict.get(n, []):
            dfs(adj)
        
        for i in range(n):
            if i not in visited:
                count += 1
            
        dfs(i)
        return count
  
  
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        # Build adjacency list
        adj_dict = defaultdict(list)
        
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
        
        visited = set()
        
        def bfs(start):
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                visited.add(node)
                
                for neighbor in adj_dict[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        
        return res
  
  
edges1 = [[0,1], [1,2], [3,4]]
print(Solution323().countComponents(5, edges1))

edges2 = [[0,1], [1,2], [2,3], [3,4]]
print(Solution323().countComponents(5, edges2))