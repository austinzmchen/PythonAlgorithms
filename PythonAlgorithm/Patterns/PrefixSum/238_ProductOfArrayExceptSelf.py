class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            prefix[i] = p
            p *= nums[i] 

        p = 1
        postfix = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = p
            p *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res


#       [ 1, 2, 3, 4]
# left: [ 1, 1, 2, 6]
# right:[24,12, 4, 1]
# res:  [12,12, 8, 6]