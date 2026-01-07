
class Solution:
    
    # TLE
    def lengthOfLIS(self, nums: List[int]) -> int:
        import sys
        from functools import lru_cache

        @lru_cache
        def recur(i, frm, count):
            if i >= len(nums):
                return count
            
            c = 0
            if nums[i] > frm:
                c = recur(i + 1, nums[i], count + 1)

            return max(
                c,
                recur(i + 1, frm, count),   # not select this
                recur(i + 1, nums[i], 1)    # start with this
            )
        
        return recur(0, -sys.maxsize-1, 0)
    