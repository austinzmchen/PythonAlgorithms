from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #
        _dict = defaultdict(int)
        for n in nums:
            _dict[n] += 1
        #
        _min = []
        for n, f in _dict.items():
            if len(_min) < k:
                heappush(_min, (f, n))
            else:
                if f > _min[0][0]:
                    heappop(_min)
                    heappush(_min, (f, n))
        #
        return [v[1] for v in _min]
            
            
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))