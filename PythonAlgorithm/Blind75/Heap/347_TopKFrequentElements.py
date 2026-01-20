from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = {}
        for n in nums:
            _dict[n] = _dict.get(n, 0) + 1

        min_heap = []
        for n, f in _dict.items():
            if len(min_heap) < k:
                heappush(min_heap, (f, n))
            else:
                if f > min_heap[0][0]:
                    heappop(min_heap)
                    heappush(min_heap, (f, n))

        return [t[1] for t in min_heap]

    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        min_heap = []
        for n, f in Counter(nums).items():
            if len(min_heap) < k:
                heappush(min_heap, (f, n))
            else:
                if f > min_heap[0][0]:
                    heappop(min_heap)
                    heappush(min_heap, (f, n))

        return [t[1] for t in min_heap]
    
    
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))