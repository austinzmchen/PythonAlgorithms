from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache

        @lru_cache
        def recur(i):
            # if not all words match, idx would be stuck before the end of list
            if i >= len(s):
                return True
            
            found = False
            for j in range(i + 1, len(s) + 1):
                w = s[i: j]

                if w in wordDict:
                    found = found or recur(j)
            return found

        return recur(0)