class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        import sys
        curr_sum, res = 0, -sys.maxsize-1
        
        for n in nums:
            if n > curr_sum + n: # if 0 > _sum:
                curr_sum = n
            else:
                curr_sum += n
            res = max(res, curr_sum)
            
        return res
    
    
    # also works
    def maxSubArray(self, nums: list[int]) -> int:
        import sys
        curr_sum, res = 0, -sys.maxsize-1
        
        for n in nums:
            curr_sum = max(n, curr_sum + n)
            res = max(res, curr_sum)
            
        return res
    
    
    def maxSubArray2(self, nums: list[int]) -> int:
        def recur(i, must_pick: bool):
            if i >= len(nums):
                return 0
            
            if must_pick:
                # stop here or continue
                return max(nums[i], recur(i+1, True) + nums[i])
            else:
                # If we don't have to pick, we can skip or start picking
                return max(recur(i+1, False), recur(i, True))
        
        return recur(0, False)
    

print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))