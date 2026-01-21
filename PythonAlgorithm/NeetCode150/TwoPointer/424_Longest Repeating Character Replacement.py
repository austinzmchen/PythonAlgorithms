class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        _dict = {}
        curr_max = 0
        
        l = 0
        for r, c in enumerate(s):
            _dict[c] = _dict.get(c, 0) + 1
            curr_max = max(curr_max, _dict[c])

            # not enough to k to replace, inc l to find next max
            while l < r and curr_max + k < r - l + 1:
                _dict[s[l]] -= 1
                curr_max = max(_dict.values())
                
                l += 1

            res = max(res, r - l + 1)
        
        # longest substring containing the same letter, e.g.: "AABA"
        return res
    