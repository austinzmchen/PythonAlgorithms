class Solution:
    """
    Kadane’s Algorithm is based on one simple observation:
        if the running sum becomes negative, keeping it will only reduce the sum of any future subarray
    """
    def maxSubArray2(self, nums: list[int]) -> int:
        import sys
        curr_sum, res = 0, -sys.maxsize-1
        
        for n in nums:
            if n > curr_sum + n: # if 0 > curr_sum:
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
    
    
    def maxSubArray(self, nums: list[int]) -> int:
        def recur(i, must_pick: bool):
            if i >= len(nums):
                return 0
            
            if must_pick:
                # stop here or continue
                return max(nums[i], 
                           recur(i + 1, True) + nums[i])
            else:
                # If we don't have to pick, we can skip or start picking
                return max(recur(i + 1, False), 
                           recur(i, True))
        
        return recur(0, False)
    
    
    # NOT working, because skipping can not be together with continuing since it is a continous array
    def maxSubArray(self, nums: list[int]) -> int:
        def recur(i, curr_sum):
            if i >= len(nums):
                return 0

            # either stop pikcing, or continue or start picking or skipping
            return max(
                curr_sum + nums[i], # stop
                recur(i + 1, curr_sum + nums[i]), # continue
                recur(i + 1, nums[i]), # start picking
                recur(i + 1)
            )
        return recur(0, 0)
    
    
    # Not working on nums = [-1]
    def maxSubArray(self, nums: List[int]) -> int:
        def recur(i, curr_sum, pick):
            if i >= len(nums):
                return curr_sum
            
            if not pick:
                return max(
                    recur(i + 1, nums[i], True), # start
                    recur(i + 1, 0, False) # skip
                )
            else:
                return max(
                    curr_sum + nums[i], # stop
                    recur(i + 1, curr_sum + nums[i], True), # continue   
                )
        
        return recur(0, 0, False)
    

print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
