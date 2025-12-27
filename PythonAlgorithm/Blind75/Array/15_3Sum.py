from typing import List

# https://fizzbuzzed.com/top-interview-questions-1/
class Solution15:
      
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # for avoiding duplicates
        res = []
        
        for i in range(0, len(nums) - 2):
            # avoid duplicates
            if i-1>=0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            _set = set()

            j = i + 1
            while j < len(nums):
                if target - nums[j] in _set:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])
                    # avoid duplicates
                    while i+1 < j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1

                _set.add(nums[j])
                j += 1

        return res
                    
    
    # Not seem to work! leetcode submission failed 
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            # avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            _set = set()

            j = i + 1
            while j < len(nums):
                # print(f"diff: {target - nums[j]}, map: {_map.keys()}")
                if target - nums[j] in _set:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])
                    # avoid duplicates
                    if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 2
                        continue

                _set.add(nums[j])
                j += 1

        return res

    
    # this is more intuitive, and something i can remember
    # TLE on hundres of 0 as input
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # track indexes
        res: list[list] = []

        for i, n in enumerate(nums[:-2]):
            _dict = {}
            for j, n2 in enumerate(nums[i+1:], start=i+1):
                _dict[n2] = j

            for j, n2 in enumerate(nums[i+1:], start=i+1):
                remain = 0-n-n2
                if (idx := _dict.get(remain)) is not None and idx != j:
                    res.append([i, j, idx])
        
        # get num value from indexes
        res = [[nums[ls[0]], nums[ls[1]], nums[ls[2]]] 
               for ls in res]
        # dedup by num value
        return list({tuple(sorted(ls)) for ls in res})


print(Solution15().threeSum([-1,0,1,2,-1,-4]))
# print(Solution15().threeSum([0,0,0,0]))

