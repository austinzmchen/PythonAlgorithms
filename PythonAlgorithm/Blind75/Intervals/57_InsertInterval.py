from typing import List

class Solution:    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        for inv in intervals:
            if inv[1] < newInterval[0]:
                res.append(inv)
            else:
                break
            i += 1
        
        start, end = newInterval

        for _, inv in enumerate(intervals[i:], start=i):
            if inv[0] <= end:
                start = min(start, inv[0])
                end = max(end, inv[1])
            else:
                res.append((start, end))
                start, end = inv[0], inv[1]

        res.append((start, end))
        return res
    
    
    # just include it in then sort and merge
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        res = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            inv = intervals[i]
            if inv[0] <= end:
                start = min(start, inv[0])
                end = max(end, inv[1])
            else:
                res.append([start, end])
                start, end = inv
        
        res.append([start, end])
        return res
    

print(Solution().insert([[1,5]], [6, 8]))