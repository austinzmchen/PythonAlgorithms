from typing import List

# not tested
class Solution:
    def minimumCost(N: int, connections: List[List[int]]):
        dict = []
        for c in connections:
            p1, p2, cost = c
            dict[(p1,p2)] = cost
            dict[(p2,p1)] = cost
        #
        visited = set()
        min_heap = [(0, 1)]
        min_cost = 0
        while len(min_heap) > 0:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            min_cost += cost
            visited.add(node)
            for i in range(1, N+1):
                if i not in visited:
                    if d := dict.get((i, node)):
                        heapq.heappush(min_heap, (d, i))
            #
        return min_cost if len(visited) == N else -1