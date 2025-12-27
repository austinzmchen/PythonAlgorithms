from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
          merged.append(list(intervals[i]))
          i += 1
        
        curr = list(newInterval)
        for j in range(i, len(intervals)):
          inv = intervals[j]
          if inv[0] <= curr[1]:
            curr = [min(curr[0], inv[0]), max(curr[1], inv[1])]
          else:
            merged.append(curr)
            curr = list(inv)

        merged.append(curr)
        return merged
    
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        for inv in intervals:
            if inv[1] < newInterval[0]:
                res.append(inv)
            else:
                break
            i += 1
        
        start, end = newInterval[0], newInterval[1]

        for _, inv in enumerate(intervals[i:], start=i):
            if inv[0] <= end:
                start = min(start, inv[0])
                end = max(end, inv[1])
            else:
                res.append((start, end))
                start, end = inv[0], inv[1]

        res.append((start, end))
        return res
      

print(Solution().insert([[1,5]], [6, 8]))