from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        max_heap = []

        for i, p in enumerate(points):
            length = p[0] ** 2 + p[1] ** 2

            if len(max_heap) < k:
                heappush(max_heap, (-length, i))
            
            else:
                if length < -max_heap[0][0]:
                    heappop(max_heap)
                    heappush(max_heap, (-length, i))
        
        return [points[t[1]] for t in max_heap]
    

print(Solution().kClosest([[-5,4], [-6,-5], [4,6]], 2))