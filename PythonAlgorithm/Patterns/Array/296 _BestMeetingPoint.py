from typing import List
import sys

# not the most optimal solution
class Solution:
    def minTotalDistance(self, grid: List[List[int]]):
        _min_cood = (0,0)
        _min = sys.maxsize
        targets = []
        #
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    targets.append((i,j))
        #
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                total = 0
                for t in targets:
                    total += abs(i - t[0]) + abs(j - t[1])
                if total < _min:
                  _min = total
                  _min_cood = (i,j)
        #
        return _min
      

print(Solution().minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))