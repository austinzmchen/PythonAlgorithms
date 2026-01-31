def lengthOfLongestSubstring(self, s: str) -> int:
    l, _set = 0, set()
    res = 0

    for r, c in enumerate(s):
        while l < r and c in _set:
            lc = s[l]
            _set.discard(lc)
            l += 1

        res = max(res, r - l + 1)
        _set.add(c)
    
    return res
