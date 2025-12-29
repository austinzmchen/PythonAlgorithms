from typing import List

# use dictionary because image input as 1, -1, 0
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        prefix_sum = {0:1}
        count = 0
        #
        for n in nums:
            sum += n
            if (sum - k) in prefix_sum:
                count += prefix_sum[sum-k]
            if sum in prefix_sum:
                prefix_sum[sum] += 1
            else:
                prefix_sum[sum] = 1
        #
        return count