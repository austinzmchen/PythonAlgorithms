class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        @lru_cache
        def recur(i1, i2):
            if i2 == len(t):
                return 1
            if i1 == len(s):
                return 0
            
            c = 0
            if s[i1] == t[i2]:
                c = recur(i1 + 1, i2 + 1)
            
            return c + recur(i1 + 1, i2)
        return recur(0, 0)
    
    
    # TLE
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        @lru_cache
        def recur(i, path):
            if i == len(s):
                return 1 if path == t else 0
            
            return recur(i + 1, path + s[i]) + recur(i + 1, path)
        return recur(0, "")