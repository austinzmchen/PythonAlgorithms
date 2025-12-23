class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _dict = {}
        for c in s:
            _dict[c] = _dict.get(c, 0) + 1

        for c in t:
            if c not in _dict:
                return False

            _dict[c] -= 1
            if _dict[c] == 0:
                _dict.pop(c)

        return len(_dict) == 0