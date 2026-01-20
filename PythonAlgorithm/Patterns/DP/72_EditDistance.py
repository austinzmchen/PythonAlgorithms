
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import lru_cache
        
        @lru_cache
        def recur(i, j):
            if i == len(word1):
                # remove the rest chars
                return len(word2) - j
            
            elif j == len(word2):
                # add the rest chars
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return recur(i + 1, j + 1)
            
            # insert, delete, or replace
            return 1 + min(recur(i + 1, j), 
                            recur(i, j + 1), 
                            recur(i + 1, j + 1))
        
        return recur(0, 0)