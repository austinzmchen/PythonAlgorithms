from functools import lru_cache
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        import sys
        @lru_cache
        def recur(x, y):
            if x == len(grid)-1 and y == len(grid[0])-1:
                return grid[x][y]
            if x == len(grid) or y == len(grid[0]):
                return sys.maxsize
            
            return min(recur(x+1,y), recur(x, y+1)) + grid[x][y]
        #
        return recur(0, 0)
      
    
    def minPathSum2(self, grid: List[List[int]]) -> int:
        import sys
        dp = [[0 for _ in row] for row in grid]
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                    continue
                #
                up = dp[row-1][col] if row >= 1 else sys.maxsize
                left = dp[row][col-1] if col >= 1 else sys.maxsize
                
                dp[row][col] = min(up, left) + grid[row][col]
                print(f'left: {left}, up: {up}, before: {grid[row][col]}, after: {dp[row][col]}')
        #
        return dp[-1][-1]
      
      
print(Solution().minPathSum2([[1,3,1],[1,5,1],[4,2,1]]))