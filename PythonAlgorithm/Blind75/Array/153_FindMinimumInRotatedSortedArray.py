class Solution153:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # check no rotation
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            mid = l + (r - l) // 2
            if mid+1 < len(nums) and nums[mid+1] < nums[mid]:
                return nums[mid+1]
            elif mid-1 >= 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            #
            if nums[l] < nums[mid]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1

        return -1
    
    
    # submitted and passed
    def findMin2(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if (mid - 1) >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] < nums[r]:
                # if right half is increasing
                # the the min num is at the left half
                r = mid
            else:
                l = mid + 1
        
        return nums[r]
    

print(Solution153().findMin2([10, 15, 1, 3, 8]))
print(Solution153().findMin2([4, 5, 7, 9, 10, -1, 2]))
print(Solution153().findMin2([1, 3, 8, 10]))