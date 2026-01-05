from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import sys

        def recur(i, curr, count):
            if i >= len(nums):
                return count
            
            c = -sys.maxsize-1
            if nums[i] > curr:
                c = recur(i+1, nums[i], count+1)

            return max(
                c,
                recur(i+1, curr, count),
                recur(i+1, nums[i], 1)
            )
        
        return recur(0, -sys.maxsize-1, 0)