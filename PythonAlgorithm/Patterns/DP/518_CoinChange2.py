from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        
        @lru_cache(maxsize=None)
        def recur(i, n):
            if i == len(coins) or n < 0:
                return 0
            if n == 0:
                return 1
            # select current again or skip
            return recur(i, n - coins[i]) + recur(i + 1, n)

        return recur(0, amount)