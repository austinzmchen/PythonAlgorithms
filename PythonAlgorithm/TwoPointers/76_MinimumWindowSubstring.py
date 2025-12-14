from collections import defaultdict


class Solution76:
    def minWindow(self, s: str, t: str) -> str:
        _dict = defaultdict(int)
        for c in t:
            _dict[c] += 1
        c_count = len(_dict)
        #
        l, r = 0, 0
        import sys
        start, _len = -1, sys.maxsize
        while r < len(s):
            if s[r] in _dict:
                _dict[s[r]] -= 1
                if _dict[s[r]] == 0:
                    c_count -= 1
            #
            while l < len(s) and c_count == 0:
                if s[l] in _dict:
                    if _dict[s[l]] == 0:
                        c_count += 1
                    _dict[s[l]] += 1
                #
                if r-l+1 < _len:
                    start = l 
                    _len = r-l+1
                #
                l += 1
            #
            r += 1
        #
        return s[start:start+_len] if start != -1 else ""
         
                
print(Solution76().minWindow('aa', 'aa'))