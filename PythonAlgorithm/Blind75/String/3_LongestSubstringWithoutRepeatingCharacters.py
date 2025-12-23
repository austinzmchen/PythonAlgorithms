def lengthOfLongestSubstring(self, s: str) -> int:
    win_s, _set = 0, set()
    res = 0

    for win_e, c in enumerate(s):
        while win_s < win_e and c in _set:
            lc = s[win_s]
            _set.discard(lc)
            win_s += 1

        res = max(res, win_e - win_s + 1)
        _set.add(c)
    
    return res
