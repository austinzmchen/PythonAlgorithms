from typing import List
from heapq import heappush, heappop

class Solution215:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heappush(min_heap, n)
                continue
            if n > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, n)
        #
        return min_heap[0]
      
print(Solution215().findKthLargest([-1, 2, 0], 2))