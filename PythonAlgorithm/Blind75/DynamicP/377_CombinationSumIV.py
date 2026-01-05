from typing import List

class Solution:
    
    # This is not working probably because (1, 3) and (3, 1)
    # are both valid ansers, which this code does not account for
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def recur(idx, curr_sum):
            if idx >= len(nums):
                return 0
            if curr_sum > target:
                return 0
            if curr_sum == target:
                return 1
            
            return recur(idx, nums[idx] + curr_sum) + \
                    recur(idx + 1, curr_sum)
        
        return recur(0, 0)
    
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from functools import lru_cache
        
        @lru_cache
        def recur(curr_sum):
            if curr_sum > target:
                return 0
            if curr_sum == target:
                return 1
            
            count = 0
            for n in nums:
                count += recur(curr_sum + n)
            return count
        return recur(0)
    
    
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
print(Solution().combinationSum4([1,2,3], 4))