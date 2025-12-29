from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def recur(i, curr_sum, first_i):
            if i == len(nums) - 1:
                if first_i == 0:
                    return curr_sum

            if i >= len(nums):
                return curr_sum
            
            return max(recur(i + 2, curr_sum + nums[i], i),
                        recur(i + 1, curr_sum, -1))
        
        return recur(0, 0, -1)
    

print(Solution().rob([2,3,2]))
print(Solution().rob([1,2,3]))