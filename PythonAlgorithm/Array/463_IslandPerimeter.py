from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        _sum = 0
        def recur(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[r]):
                return 0
            if grid[r][c] == 0:
                return 0
            if grid[r][c] == -1:
                return 1
            #
            grid[r][c] = -1
            nonlocal _sum
            a = (recur(r+1, c) + recur(r, c+1) + recur(r-1, c) + recur(r, c-1))
            _sum = _sum + 4 - a
            grid[r][c] = 1
            return 1
        #
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    recur(i, j)
                    return _sum
        #
        return -1
      

print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(Solution().islandPerimeter([[0,1],[0,1]]))