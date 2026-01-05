from typing import List


class Solution:
    
    def jump(self, nums: List[int]) -> int:
        from functools import lru_cache

        @lru_cache
        def recur(idx, curr):
            if idx >= len(nums) - 1:
                return curr
            
            import sys
            res = sys.maxsize

            for j in range(1, nums[idx] + 1):
                res = min(res, recur(idx + j, curr + 1))
            
            return res
        
        return recur(0, 0)