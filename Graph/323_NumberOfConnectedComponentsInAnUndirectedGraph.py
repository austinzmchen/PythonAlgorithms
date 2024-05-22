
class Solution323:
  
  def countComponents(self, n: int, edges: list) -> int:
    adj_dict = {i: [] for i in range(n)}
    
    for e in edges:
      adj_dict[e[0]].append(e[1])
      adj_dict[e[1]].append(e[0])
      
    def dfs(n, visited):
      if n in visited:
        return
      #
      visited.add(n)
      for adj in adj_dict[n]:
        dfs(adj, visited)
    
    count = 0
    visited = set()
    for i in range(n):
      if i not in visited:
        count += 1
      dfs(i, visited)
    #
    return count
  
  
edges1 = [[0,1], [1,2], [3,4]]
print(Solution323().countComponents(5, edges1))

edges2 = [[0,1], [1,2], [2,3], [3,4]]
print(Solution323().countComponents(5, edges2))