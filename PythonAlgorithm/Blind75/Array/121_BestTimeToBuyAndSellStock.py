class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        import sys
        low, max_profit = sys.maxsize, 0
        
        for p in prices:
            low = min(low, p)
            max_profit = max(max_profit, p - low)
            
        return max_profit
    