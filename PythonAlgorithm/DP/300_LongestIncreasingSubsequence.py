from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import math
        @lru_cache(maxsize=None)
        def recur(i, prev):
            if i == len(nums):
                return 0
            c = 0
            if nums[i] > prev:
                c = 1 + recur(i+1, nums[i])
            return max(c, recur(i + 1, prev))
        #
        return recur(0, -math.inf)