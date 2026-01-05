class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from functools import lru_cache

        @lru_cache
        def recur(i, curr_sum):
            if i >= len(nums):
                return 1 if curr_sum == target else 0
            
            return recur(i + 1, nums[i] + curr_sum) + \
                    recur(i + 1, -nums[i] + curr_sum)
        
        return recur(0, 0)