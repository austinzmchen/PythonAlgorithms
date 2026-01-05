from functools import lru_cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.recur(s, 0, len(s) -1)
    
    @lru_cache
    def recur(self, s: str, s_idx, e_idx) -> str:
        if s_idx > e_idx:
            return ""
        elif s_idx == e_idx:
            return s[s_idx]
        #
        if s[s_idx] == s[e_idx]:
            _str = self.recur(s, s_idx+1, e_idx-1)
            if len(_str) + 2 == e_idx - s_idx + 1:
                return s[s_idx:e_idx+1]
        #
        s1 = self.recur(s, s_idx, e_idx-1)
        s2 = self.recur(s, s_idx+1, e_idx)
        if len(s1) >= len(s2):
            return s1
        else:
            return s2
          

class Solution2:
    
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def recur(l, r):
            if l == r:
                return 1
            if l > r:
                return 0

            c = 0
            if s[l] == s[r]:
                c = recur(l + 1, r - 1) + 2

                nonlocal res
                if c > len(res):
                    res = s[l : r+1]
            
            return max(
                c,
                recur(l + 1, r),
                recur(l, r - 1),
            )
        
        recur(0, len(s) - 1)
        return res
      
      
print(Solution2().longestPalindrome("babad"))
print(Solution2().longestPalindrome("cbbd"))