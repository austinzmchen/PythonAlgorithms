
from collections import defaultdict
from typing import List


class Solution:
    def can_chain_words(self, list_words: List[str]):
        first_letter_dict = defaultdict(list)
        for w in list_words:
            first_letter_dict[w[0]].append(w)
        #
        dict = defaultdict(list)
        for w in list_words:
            ls = first_letter_dict[w[-1]]
            _set = set(ls)
            _set.discard(w) # exclude self that first letter and last letter the same
            dict[w] = list(_set)
        #
        for w in list_words:
            visited = set()
            q = [w]
            while len(q) > 0:
                wn = q.pop(0)
                if wn in visited:
                    return True
                visited.add(wn)
                for adj in dict[wn]:
                    q.append(adj)
        #
        return False
            
      
print(Solution().can_chain_words(["eve", "eat", "ripe", "tear"]))
print(Solution().can_chain_words(["eve", "eat", "rip", "tear"]))