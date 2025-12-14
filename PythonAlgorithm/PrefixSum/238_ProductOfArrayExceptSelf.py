class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _sum = 1
        #
        prefix_sum = [0] * len(nums)
        for i in range(len(nums)):
            prefix_sum[i] = _sum
            _sum *= nums[i] 
        #
        _sum = 1
        postfix_sum = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            postfix_sum[i] = _sum
            _sum *= nums[i]
        #
        res = []
        for i in range(len(nums)):
            res.append(prefix_sum[i] * postfix_sum[i])
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product *= n
        #
        r = [0] * len(nums)
        if zero_count > 1:
            return r
        else:
            for i, n in enumerate(nums):
                if zero_count == 1 and n != 0:
                    r[i] = 0
                elif n == 0:
                    r[i] = product
                else:
                    r[i] = product // n
            return r