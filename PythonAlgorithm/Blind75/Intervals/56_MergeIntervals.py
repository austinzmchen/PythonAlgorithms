from typing import List

class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda ls: ls[0])
        start, end = intervals[0]
        res = []

        for _, inv in enumerate(intervals[1:], start=1):
            if inv[0] <= end:
                start = min(start, inv[0])
                end = max(end, inv[1])
            else:
                res.append((start, end))
                start, end = inv
        
        res.append((start, end))
        return res