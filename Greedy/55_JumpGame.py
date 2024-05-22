from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def recur(i):
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            
            can = False
            for j in range(i+1, i+nums[i] + 1):
                can = can or recur(j)
            return can

        return recur(0)