from typing import List


class Solution128:
    def longestConsecutive1(self, nums: List[int]) -> int:
      _set = set(nums)
      
      _max = 0
      for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in _set:
            count = 1
            m = n + 1
            while m in _set:
                m += 1
                count += 1
            _max = max(_max, count)

      return _max
  
  
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
