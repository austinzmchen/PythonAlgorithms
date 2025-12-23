from collections import defaultdict


class Solution76:
    def minWindow_1(self, s: str, t: str) -> str:
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
         
    
    # two pointers, sliding window
    # NO WORKING !!
    def minWindow(self, s: str, t: str) -> str:
        _dict = {}
        for c in t:
            _dict[c] = _dict.get(c, 0) + 1
        
        import sys
        win_s = 0
        min_length, res = sys.maxsize, ""

        for win_e, c in enumerate(s):
            if c in _dict:
                _dict[c] -= 1
                if _dict[c] == 0:
                    del _dict[c] # this is WRONG! should not delete
                    # _dict[c] can be negative by win_e, but added to 0 by win_s
            
            while not _dict:
                char_s = s[win_s]
                if char_s in t:
                    _dict[char_s] = _dict.get(char_s, 0) + 1
                    print(f"{char_s=}, {win_s=}, {win_e=}, {_dict=}")
                
                if win_e - win_s + 1 < min_length:
                    min_length = win_e - win_s + 1
                    res = s[win_s:win_e+1]
                    
                win_s += 1
        return res
    

print(Solution76().minWindow("ADOBECODEBANC", "ABC"))
# print(Solution76().minWindow('aa', 'aa'))