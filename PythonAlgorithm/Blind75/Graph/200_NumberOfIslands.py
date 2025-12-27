
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recur(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
                return
            if grid[x][y] == '0':
                return
            grid[x][y] = '0'
            recur(x-1, y)
            recur(x, y-1)
            recur(x+1, y)
            recur(x, y+1)

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == '1':
                    count += 1
                    recur(x, y)

        return count