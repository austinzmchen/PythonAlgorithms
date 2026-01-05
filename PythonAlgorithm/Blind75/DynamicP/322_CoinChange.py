from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import sys
        coins.sort(reverse=True)
        #
        @lru_cache(maxsize=None)
        def recur(idx, n):
            if idx == len(coins) or n < 0:
                return sys.maxsize
            if n == 0:
                return 0
            a = recur(idx, n-coins[idx])
            if a != sys.maxsize: 
              a += 1
            #
            b = recur(idx+1, n)
            return min(a, b)
        #
        r = recur(0, amount)
        return -1 if r == sys.maxsize else r
      

import math
from functools import lru_cache

class Solution322:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True) # optimization, bigger coins at the end
        
        @lru_cache(maxsize=None)
        def recur(idx, count, _sum):
            if idx >= len(coins) or _sum < 0:
                return math.inf
            if _sum == 0:
                return count
            
            # either select current, or skip
            return min(recur(idx, count+1, _sum-coins[idx]),
                       recur(idx+1, count, _sum))

        r = recur(0, 0, amount)
        return -1 if r == math.inf else r
      
      
print(Solution322().coinChange([1,2,5], 11))