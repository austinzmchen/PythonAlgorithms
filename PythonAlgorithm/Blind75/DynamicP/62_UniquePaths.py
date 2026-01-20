
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache
        def recur(r, c):
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            return recur(r + 1, c) + recur(r, c + 1)

        return recur(0, 0)