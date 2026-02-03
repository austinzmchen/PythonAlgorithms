# Description
# You are given a m x n 2D grid initialized with these three possible values:
#
# `-1` - A water cell that can not be traversed.
# `0` - A treasure chest.
# `INF` - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
#
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.
# Modify the grid in-place.

class Solution:
    def walls_and_gates(self, grid: List[List[int]]) -> None:
        from collections import deque
        queue = deque()
        visited = set() # use set since i can not set value in grid

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 0:
                    queue.append((r, c))

        def bfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]):
                return
            if grid[r][c] <= 0:
                return
            if (r, c) in visited:
                return
            
            queue.append((r, c))
            visited.add((r, c))

        dist = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                grid[r][c] = dist
                
                bfs(r - 1, c)
                bfs(r + 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
                
            dist += 1
        return
    
    
input = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Solution().walls_and_gates(input)

for ls in input:
    print(ls)


input2 = [
  [0,-1],
  [2147483647,2147483647],
]
Solution().walls_and_gates(input2)

for ls in input2:
    print(ls)