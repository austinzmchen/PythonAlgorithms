class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def recur(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
                return 0
            if grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0

            count = 1
            count += recur(x - 1, y) + \
                    recur(x + 1, y) + \
                    recur(x, y - 1) + \
                    recur(x, y + 1)
            return count
        
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    res = max(res, recur(x, y))

        return res
    

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(grid))