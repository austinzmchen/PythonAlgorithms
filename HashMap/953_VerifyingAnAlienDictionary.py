class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        _dict = {}
        for i, c in enumerate(order):
            _dict[c] = i
        #
        for j in range(1, len(words)):
            w1 = words[j-1]
            w2 = words[j]
            #
            idx = 0
            while idx < len(w1) and idx < len(w2):
                if _dict[w1[idx]] < _dict[w2[idx]]:
                    break
                elif _dict[w1[idx]] > _dict[w2[idx]]:
                    return False
                idx += 1
            else:
                if len(w1) > len(w2):
                    return False
        #
        return True