from functools import lru_cache
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache

        @lru_cache
        def recur(idx):
            # if not all words match, idx would be stuck before the end of list
            if idx >= len(s):
                return True
            
            for i in range(idx + 1, len(s) + 1):
                w = s[idx: i]

                if w in wordDict:
                    if recur(i): # i is not in previous word
                        return True
            return False

        return recur(0)