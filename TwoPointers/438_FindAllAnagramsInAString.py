from typing import DefaultDict, List


class Solution438:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict = DefaultDict(int)
        match = 0
        for c in p:
            if c not in dict:
                match += 1
            dict[c] += 1
        #
        res = []
        winE = winS = 0
        while winE < len(s):
            if s[winE] in dict:
                dict[s[winE]] -= 1
                if dict[s[winE]] == 0:
                    match -= 1
            #
            if winE - winS >= len(p):
                if s[winS] in dict:
                    if dict[s[winS]] == 0:
                        match += 1
                    dict[s[winS]] += 1
                winS += 1
            #
            if match == 0:
                res.append(winS)
            #
            winE += 1
        #
        return res