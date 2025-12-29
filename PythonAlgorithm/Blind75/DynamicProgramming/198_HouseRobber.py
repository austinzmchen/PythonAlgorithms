from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def recur(idx, curr_sum):
            if idx >= len(nums):
                return curr_sum
            
            return max(recur(idx + 2, nums[idx] + curr_sum), 
                        recur(idx + 1, curr_sum))

        return recur(0, 0)