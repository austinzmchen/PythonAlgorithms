
from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = set()
        
        @lru_cache(maxsize=None)
        def recur(l, r):
            if l > r:
                return 0
            if l == r:
                res.add((l,r))
                return 1
            #
            _len = 0
            
            if s[l] == s[r]:
                v = recur(l+1, r-1)
                if v + 2 == r-l+1:
                    res.add((l,r))
                    _len = v + 2
            #
            return max(_len, recur(l+1, r), recur(l, r-1))
        #
        recur(0, len(s)-1)
        return len(res)

    def countSubstrings(self, s: str) -> int:
        count = 0
        cache = {}
        #
        def isValid(s: str, i, j):
            e = j - 1
            while i < e:
                if s[i] != s[e]:
                    return False
                i += 1
                e -= 1
            return True
        #
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                if v := cache.get(s[i:j]):
                    count += 1 if v else 0
                    continue
                if valid := isValid(s, i, j):
                    count += 1
                cache[s[i:j]] = valid
        #
        return count
      
      