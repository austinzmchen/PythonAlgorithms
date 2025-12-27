from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        import sys
        curr_min = curr_max = 1
        res = -sys.maxsize-1

        for _, n in enumerate(nums):
            # If current number is negative, swap max and min
            # because multiplying by negative flips the signs
            if n < 0:
                curr_max, curr_min = curr_min, curr_max

            # either choose current n or product it to currrent
            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)

            res = max(res, curr_max)
        return res
    
    
    # Not working!
    # The tricky part about this problem compared to maximum sum subarray is handling negative numbers:
    def maxProduct0(self, nums: List[int]) -> int:
        import sys
        curr = 1
        res = -sys.maxsize-1

        for n in nums:
            if n > curr * n:
                curr = n
            else:
                curr *= n

            res = max(res, curr)
        return res
    
print(Solution().maxProduct([-2,3,-4]))