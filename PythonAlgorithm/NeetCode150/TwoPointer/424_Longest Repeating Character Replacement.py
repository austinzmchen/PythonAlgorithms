class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        _dict = {}
        l = 0
        curr_max = 0

        for r, c in enumerate(s):
            _dict[c] = _dict.get(c, 0) + 1
            curr_max = max(curr_max, _dict[c])

            while curr_max + k < r - l + 1:
                _dict[s[l]] -= 1
                
                l += 1
                curr_max = max(_dict.values())

            res = max(res, r - l + 1)

        return res
    