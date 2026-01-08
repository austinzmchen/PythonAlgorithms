class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _dict = {}
        char_count = 0
        for c in s1:
            if c not in _dict:
                char_count += 1
            _dict[c] = _dict.get(c, 0) + 1

        l = 0
        for r, c in enumerate(s2):
            if c in _dict:
                _dict[c] -= 1
                if _dict[c] == 0:
                    char_count -= 1
            
            if r >= len(s1):
                if s2[l] in _dict:
                    _dict[s2[l]] += 1
                    if _dict[s2[l]] == 1:
                        char_count += 1
                l += 1
            
            if char_count == 0:
                return True
        
        return False

        
print(Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo"))