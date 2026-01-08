class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # too hard
        # just do brute force
        
        nums = sorted(nums1 + nums2)
        l, r = 0, len(nums) - 1
        
        while l < r:
            l += 1
            r -= 1
        
        if l == r:
            return nums[l]
        else:
            return (nums[l - 1] + nums[r + 1]) / 2