from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum = sum(nums)
        if _sum % k != 0:
            return False
        buckets = [_sum / k] * k
        nums.sort(reverse=True) ## place bigger number first to improve run time
        #
        def recur(idx):
            if idx == len(nums):
                return True
            for i in range(k):
                if buckets[i] >= nums[idx]:
                    buckets[i] -= nums[idx]
                    if recur(idx+1):
                        return True
                    buckets[i] += nums[idx]
                    if buckets[i] == _sum / k: # because this algorithm always fill the previous buckets before trying the next.
                        break
            return False
        #
        return recur(0)
                