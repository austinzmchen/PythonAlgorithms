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
            key = "".join(sorted(s))
            _dict.setdefault(key, []).append(s)
        
        return list(_dict.values())


print(Solution().groupAnagrams2(strs = ["eat","tea","tan","ate","nat","bat"]))