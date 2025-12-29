class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1):
            res = res ^ i
        for v in nums:
            res = res ^ v
        return res