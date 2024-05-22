from typing import List

# https://fizzbuzzed.com/top-interview-questions-1/
class Solution15:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < len(nums) -1 and nums[l] == nums[l+1]: l += 1
                    while r > 0 and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
                    continue
                if sum < target:
                    l += 1
                else:
                    r -= 1
        #
        return res
      
      
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            # avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #
            target = -nums[i]
            _set = set()
            #
            j = i + 1
            while j < len(nums):
                # print(f"diff: {target - nums[j]}, map: {_map.keys()}")
                if target - nums[j] in _set:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])
                    # avoid duplicates
                    while i+1 < j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                #
                _set.add(nums[j])
                j += 1
        #
        return res
                    
                    
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            # avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #
            target = -nums[i]
            _set = set()
            #
            j = i + 1
            while j < len(nums):
                # print(f"diff: {target - nums[j]}, map: {_map.keys()}")
                if target - nums[j] in _set:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])
                    # avoid duplicates
                    if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 2
                        continue
                #
                _set.add(nums[j])
                j += 1
        #
        return res


print(Solution15().threeSum2([-1,0,1,2,-1,-4]))
print(Solution15().threeSum([0,0,0,0]))

