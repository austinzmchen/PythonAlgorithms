from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #
        @lru_cache(maxsize=None)
        def recur(s_idx):
            if s_idx == len(s):
                return True
            #
            for i in range(s_idx, len(s) + 1):
                w = s[s_idx:i]
                if w in wordDict:
                    if recur(i):
                        return True
            else:
                return False
        #
        return recur(s, 0)