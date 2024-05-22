from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import sys
        r = sys.maxsize
        start, end = 0, 0
        sum = 0
        #
        while end < len(nums):
            sum += nums[end]
            while sum >= target and start <= end:
                d = end - start + 1
                if d < r:
                    r = d
                sum -= nums[start]
                start += 1
            end += 1
        #
        return 0 if r == sys.maxsize else r
      
      
print(Solution().minSubArrayLen(4, [1,4,4]))
print(Solution().minSubArrayLen(6, [10, 2, 3]))
print(Solution().minSubArrayLen(15, [1,2,3,4,5]))