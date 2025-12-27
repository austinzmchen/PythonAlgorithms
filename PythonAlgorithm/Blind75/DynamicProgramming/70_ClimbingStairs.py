
class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache
        def recur(idx):
            if idx == n:
                return 1
            if idx > n:
                return 0
            
            return recur(idx+1) + recur(idx+2)
        
        return recur(0)