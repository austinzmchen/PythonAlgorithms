from functools import lru_cache
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def recur(i):
            if i == len(nums) - 1:
                return True

            can = False
            for j in range(1, nums[i] + 1):
                can = can or recur(i + j)
            return can

        return recur(0)