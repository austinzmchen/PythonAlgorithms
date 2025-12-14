from typing import List

class Solution:
  
    def merge(self, 
                  intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, 
                                    key=lambda x: x[0])
        
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