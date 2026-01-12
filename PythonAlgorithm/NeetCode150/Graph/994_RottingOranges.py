class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """ user BFS and some algorithm like topological sort
        """
        from collections import deque
        rotten_q = deque()
        fresh_count = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 2:
                    rotten_q.append((r, c))
                elif cell == 1:
                    fresh_count += 1

        if not fresh_count:
            return 0
        minute = 0

        def recur(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]):
                return
            if grid[r][c] != 1:
                return
            
            nonlocal fresh_count
            rotten_q.append((r, c))
            grid[r][c] = 2
            fresh_count -= 1
            return

        while rotten_q:
            size = len(rotten_q)
            for _ in range(size):
                r, c = rotten_q.popleft()
                recur(r - 1, c)
                recur(r + 1, c)
                recur(r, c + 1)
                recur(r, c - 1)
                
            minute += 1

        # some orange never rot
        return -1 if fresh_count != 0 else minute - 1
    

print(Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))