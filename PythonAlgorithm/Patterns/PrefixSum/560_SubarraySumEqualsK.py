from typing import List

# If we know the prefix sum at two positions, we can find the subarray sum between them:
# sum(i, j) = prefix[j] - prefix[i-1]
#  -> prefix[i-1] = prefix[j] - sum(i, j)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        res = 0
        # sum -> frequency map
        prefix = {0: 1} # there is no case of prefix[i-1]

        for n in nums:
            curr_sum += n
            
            # Check if (current_sum - k) exists
            # This means there's a subarray ending here with sum k
            if curr_sum - k in prefix:
                res += prefix[curr_sum - k]
            
            # save sum of the array ending i - 1 
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

        return res
    

print(Solution().subarraySum([1,2,1,2,1], 3)) # expect 4