from typing import List

class Solution:
    # simple brute force
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort() # remove duplicates
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]

    
    # two pointers, Passed
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # remove duplicates
        res = set() # remove duplicates
        
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -n:
                    res.add((n, nums[l], nums[r]))
                    # inc both to ignore duplicate number
                    l += 1
                    r -= 1 
                    
                elif nums[l] + nums[r] < -n:
                    l += 1
                
                else:
                    r -= 1
        
        return [list(t) for t in res]
        
        
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,0,0,0]))

