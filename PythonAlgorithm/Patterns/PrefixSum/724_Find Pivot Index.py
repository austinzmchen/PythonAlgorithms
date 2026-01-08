class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        curr_sum = 0
        prefix = [0] * len(nums)
        for i, n in enumerate(nums):
            prefix[i] = curr_sum
            curr_sum += n

        curr_sum = 0
        postfix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            postfix[i] = curr_sum
            curr_sum += n
        
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        
        return -1
