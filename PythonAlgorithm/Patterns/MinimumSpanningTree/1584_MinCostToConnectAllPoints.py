
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from heapq import heappush, heappop
        
        visited = set()
        n = len(points)
        
        min_cost = 0
        min_heap = [(0, 0)] # (cost, first point index)
        
        while len(visited) < n:
            cost, i = heappop(min_heap)
            if i in visited:
                continue

            min_cost += cost
            visited.add(i)
            x, y = points[i]
            
            for j in range(n):
                if j not in visited:
                    _x, _y = points[j]

                    distance = abs(_x - x) + abs(_y - y)
                    heappush(min_heap, (distance, j)) # heap might contain duplicates after push

        return min_cost
      
      
print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))