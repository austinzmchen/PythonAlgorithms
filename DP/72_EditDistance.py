from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def recur(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return recur(i+1, j+1)
            return min(recur(i+1, j), recur(i, j+1), recur(i+1, j+1)) + 1
        return recur(0, 0)