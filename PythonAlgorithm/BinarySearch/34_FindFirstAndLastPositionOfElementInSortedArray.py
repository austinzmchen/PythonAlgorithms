from typing import List


class Solution34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_idx = end_idx = -1
        #
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                start_idx = mid
                r = mid - 1
                continue
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        #
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                end_idx = mid
                l = mid + 1
                continue
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        #
        return [start_idx, end_idx]
      
      
sol = Solution34()
print(sol.searchRange([2,2], 2))