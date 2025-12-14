from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def recur(idx):
            if idx >= len(cost):
                return 0
            return min(cost[idx] + recur(idx+1),
                    cost[idx] + recur(idx+2))
        #
        return min(recur(0), recur(1))
        
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(cost[i] + dp[i-1],
                            cost[i] + dp[i-2],)
        return min(dp[n-1], dp[n-2])