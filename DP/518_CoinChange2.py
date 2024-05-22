from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        @lru_cache(maxsize=None)
        def recur(idx, n):
            if idx == len(coins) or n < 0:
                return 0
            if n == 0:
                return 1
            return recur(idx, n-coins[idx]) + recur(idx+1, n)
        #
        return recur(0, amount)