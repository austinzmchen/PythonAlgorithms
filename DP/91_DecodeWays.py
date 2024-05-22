from functools import lru_cache

class Solution91:
    def numDecodings(self, s: str) -> int:
      @lru_cache(maxsize=None)
      def recur(i):
        if i >= len(s):
          return 1
        if s[i] == '0':
          return 0
        
        r = recur(i+1)
        if i+1 < len(s) and \
          (s[i] == '1' or \
          s[i] == '2' and s[i+1] < '7'):
          r += recur(i+2) 
        #
        return r   
      
      return recur(0)
    
    
s = Solution91()
print(s.numDecodings('12'))
print(s.numDecodings('226'))
print(s.numDecodings('06'))
print(s.numDecodings('1201234'))