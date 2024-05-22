from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        n = len(points)
        min_cost = 0
        min_heap = [(0, 0)] # (cost, first point 0)
        while len(visited) < n:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            #
            min_cost += cost
            visited.add(node)
            for i in range(n):
                if i not in visited:
                    x, y = points[i]
                    x0, y0 = points[node]
                    distance = abs(x - x0) + abs(y - y0)
                    heapq.heappush(min_heap, (distance, i)) # heap might contain duplicates after push
        #
        return min_cost
      
      
print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))