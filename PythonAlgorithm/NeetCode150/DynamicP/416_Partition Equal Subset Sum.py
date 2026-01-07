class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from functools import lru_cache

        @lru_cache
        def recur(i, curr_sum):
            if i >= len(nums):
                return curr_sum == 0
            
            return recur(i + 1, curr_sum + nums[i]) or \
                    recur(i + 1, curr_sum - nums[i])
        
        return recur(0, 0)