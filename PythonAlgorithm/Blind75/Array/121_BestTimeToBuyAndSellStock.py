class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        import sys
        low, res = sys.maxsize, 0
        
        for p in prices:
            low = min(low, p)
            res = max(res, p - low)
            
        return res
    