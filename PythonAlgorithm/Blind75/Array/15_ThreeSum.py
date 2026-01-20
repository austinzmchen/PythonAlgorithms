from typing import List

class Solution:    
    # two pointers, Passed
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # remove duplicates
        res = set()
        
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + n == 0:
                    res.add((n, nums[l], nums[r]))
                    # inc both to ignore duplicate number
                    l += 1
                    r -= 1 
                    
                elif nums[l] + nums[r] + n < 0:
                    l += 1
                
                else:
                    r -= 1
        
        return [list(t) for t in res]
        
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,0,0,0]))

