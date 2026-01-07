from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        for _str in strs:
            s = [0] * 26
            for c in _str:
                s[ord(c) - ord('a')] += 1
            _dict[str(s)].append(_str)
        #
        return _dict.values()
            
            
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        _dict = {}

        for s in strs:
            ss = "".join(sorted(s))
            _dict.setdefault(ss, []).append(s)
        
        return [list(v) for v in _dict.values()]     