from typing import List


class Solution128:  
    def longestConsecutive(self, nums: List[int]) -> int:
        _nums = set(nums)
        res = 1

        for n in nums:
            if n - 1 in _nums:
                continue
            
            count = 0
            while n in _nums:
                count += 1
                n += 1
            
            res = max(res, count)
        return res
