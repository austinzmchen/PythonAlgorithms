
class Solution76:
    def minWindow(self, s: str, t: str) -> str:
        import sys
        from collections import Counter
        _dict = Counter(t)
        count = len(_dict)
        
        curr_min = sys.maxsize
        res = ""

        l = 0
        for r, c in enumerate(s):
            if c in _dict:
                _dict[c] -= 1
                if _dict[c] == 0:
                    count -= 1

            while count == 0 and l <= r:
                lc = s[l]
                if lc in _dict:
                    _dict[lc] += 1
                    if _dict[lc] == 1:
                        count += 1

                if r - l + 1 < curr_min:
                    curr_min = r - l + 1
                    res = s[l: l + curr_min]

                l += 1
        return res
        
        
    # two pointers, sliding window
    # NO WORKING !!
    def minWindow0(self, s: str, t: str) -> str:
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
print(Solution76().minWindow('a', 'aa'))
print(Solution76().minWindow('a', 'a'))