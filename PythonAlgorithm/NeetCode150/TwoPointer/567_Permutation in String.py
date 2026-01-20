class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        _dict = Counter(s1)
        char_count = len(_dict)
        
        l = 0
        for r, c in enumerate(s2):
            if c in _dict:
                _dict[c] -= 1
                if _dict[c] == 0:
                    char_count -= 1
            
            if r >= len(s1):
                lc = s2[l]
                if lc in _dict:
                    _dict[lc] += 1
                    if _dict[lc] == 1:
                        char_count += 1
                l += 1
            
            if char_count == 0:
                return True
        
        return False

        
print(Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo"))