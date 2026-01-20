
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import lru_cache
        
        @lru_cache
        def recur(i):
            if i >= len(cost):
                return 0
            return min(cost[i] + recur(i + 1), 
                       cost[i] + recur(i + 2))

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