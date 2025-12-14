from typing import List


class Solution128:
  def longestConsecutive(self, nums: List[int]) -> int:
    _set = set(nums)
    #
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