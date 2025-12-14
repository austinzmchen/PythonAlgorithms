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
      

print(Solution().insert([[1,5]], [6, 8]))