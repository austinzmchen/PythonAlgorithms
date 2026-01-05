class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import lru_cache

        @lru_cache
        def recur(i, hold):
            if i >= len(prices):
                return 0
            
            if hold:
                # can hold or sell
                return max(recur(i + 1, True),
                            prices[i] + recur(i + 1, False))

            else:
                # can buy or skip
                return max(-prices[i] + recur(i + 1, True),
                            recur(i + 1, False))
        
        return recur(0, False)