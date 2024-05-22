from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dict = defaultdict(list)
        [dict[arr[i]].append(i) for i in range(len(arr))]
        #
        depth = 0
        q, seen = deque([0]), set([0])
        while q:
            size = len(q)
            while size:
                i = q.popleft()
                if i == len(arr) - 1:
                    return depth
                idx_ls = [i-1, i+1] + dict[arr[i]]
                for j in set(idx_ls):
                    if 0 <= j < len(arr) and j not in seen:
                        q.append(j); seen.add(j)
                #
                dict[arr[i]] = [] # same value at diff indexes should only be tried once. avoid TLE
                size -= 1
            depth += 1
        return -1