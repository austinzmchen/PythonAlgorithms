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
      

class Solution322:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True) # optimization, bigger coins at the end
        
        import sys
        from functools import lru_cache  
        
        @lru_cache
        def recur(i, count, curr_sum):
            if i >= len(coins) or curr_sum < 0:
                return sys.maxsize
            if curr_sum == 0:
                return count
            
            # either select current, or skip
            return min(recur(i, count + 1, curr_sum - coins[i]),
                       recur(i + 1, count, curr_sum))

        res = recur(0, 0, amount)
        return -1 if res == sys.maxsize else res
      
      
print(Solution322().coinChange([1,2,5], 11))