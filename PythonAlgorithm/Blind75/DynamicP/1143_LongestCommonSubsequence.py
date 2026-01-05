class Solution:
  
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recur(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
              return 0
            
            if text1[i1] == text2[i2]:
              return 1 + recur(i1+1, i2+1)
            
            return max(recur(i1+1, i2), recur(i1, i2+1))

        return recur(0, 0)