from typing import List


class Solution523:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict = {0:-1} # reminder: index
        sum = 0
        for i, n in enumerate(nums):
            sum += n
            reminder = sum % k
            if reminder < 0:
                reminder += k
            #
            if reminder in dict:
                if i - dict[reminder] > 1:
                    return True
            else:
                dict[reminder] = i
        #
        return False
      
    
    # TLE on [1,1000000000], 1
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        sum = 0
        prefix_sum = []
        for n in nums:
          sum += n
          prefix_sum.append(sum)
        #
        dict = {0:-1}
        for i, n in enumerate(prefix_sum):
            m = n
            while n >= 0:
              if n in dict and i - dict[n] > 1:
                return True
              n -= k
            #
            if m not in dict:
              dict[m] = i
        #
        return False
    

# [23,  2,  4,  6,  7], 6
# [23, 25, 29, 35, 42], 6
# [ 5,  1,  5,  5,  0]
#
# [23,  2,  4,  6,  6], 7
# [23, 25, 29, 35, 41], 7

# print(Solution523().checkSubarraySum2([0], 1))        
print(Solution523().checkSubarraySum([5, 0, 0, 0], 3))        
            