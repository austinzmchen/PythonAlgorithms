from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        results = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            inv = intervals[i]
            if inv[0] <= curr[1]:
                curr = [curr[0], max(curr[1], inv[1])]
            else: 
                results.append(list(curr))
                curr = inv
        
        results.append(list(curr))
        return results
    
    
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
                start, end = inv[0], inv[1]
        
        res.append((start, end))
        return res