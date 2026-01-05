class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from functools import lru_cache

        @lru_cache
        def recur(i, j, str):
            if i == len(s1) and j == len(s2):
                return str == s3
            
            if i == len(s1):
                return recur(i, j + 1, str + s2[j])
            elif j == len(s2):
                return recur(i + 1, j, str + s1[i])
            else:
                return recur(i + 1, j, str + s1[i]) or \
                        recur(i, j + 1, str + s2[j])

        return recur(0, 0, "")