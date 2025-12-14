class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recur(i1, i2):
            if i1 == len(s1) or i2 == len(s2):
              return 0
            if s1[i1] == s2[i2]:
              return 1 + recur(i1+1, i2+1)
            return max(recur(i1+1, i2), recur(i1, i2+1))
        #
        return recur(0, 0)