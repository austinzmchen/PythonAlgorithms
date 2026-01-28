from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self._max = []
        self._min = []

    def addNum(self, num: int) -> None:
        if len(self._max) == 0 or num <= -self._max[0]:
            heappush(self._max, -num)
        else:
            heappush(self._min, num)
        
        # re-balance size  
        if len(self._max) > len(self._min) + 1:
            heappush(self._min, -heappop(self._max))
        elif len(self._min) > len(self._max):
            heappush(self._max, -heappop(self._min))
            

    def findMedian(self) -> float:
        if len(self._max) > len(self._min):
            return -self._max[0]
        else:
            return (-self._max[0] + self._min[0]) / 2

    
# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())