class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappush, heappop
        max_heap = []
        
        for s in stones:
            heappush(max_heap, -s)

        while len(max_heap) > 1:
            a = heappop(max_heap)
            b = heappop(max_heap)

            new = abs((-a) - (-b))
            if new  > 0:
                heappush(max_heap, -new)
        
        return -max_heap[0] if max_heap else 0