from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = defaultdict(int)
        for n in nums:
            _dict[n] += 1

        min_heap = []
        for n, f in _dict.items():
            if len(min_heap) < k:
                heappush(min_heap, (f, n))
            else:
                if f > min_heap[0][0]:
                    heappop(min_heap)
                    heappush(min_heap, (f, n))

        return [v[1] for v in min_heap]
            
    
    # submitted and passed on leetcode
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappush, heappush
        min_heap = []

        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        for num, freq in freq_map.items():
            heappush(min_heap, (freq, num))
        
        while len(min_heap) > k:
            heappop(min_heap)
        
        return [t[1] for t in min_heap]
    
    
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))