from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def recur(r, c):
            if r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            return recur(r+1, c) + recur(r, c+1)

        return recur(0, 0)
    

    def uniquePaths(self, m: int, n: int) -> int:
        def recur(mm, nn):
            if mm == 1 and nn == 1:
                return 1
            if mm < 0 or nn < 0:
                return 0
            
            return recur(mm - 1, nn) + recur(mm, nn - 1)
        return recur(m, n)