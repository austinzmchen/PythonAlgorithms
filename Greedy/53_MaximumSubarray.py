class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        _sum, _max = 0, nums[0]
        for n in nums:
            if n > _sum + n:
                _sum = n
            else:
                _sum += n
            #
            _max = max(_max, _sum)
        return _max