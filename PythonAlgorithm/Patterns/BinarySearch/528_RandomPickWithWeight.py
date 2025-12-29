import random
from typing import List

class Solution528:

    def __init__(self, w: List[int]):
        prefix_sum = [0] * len(w)
        for i in range(0, len(w)):
            prefix_sum[i] = w[i] + (0 if i == 0 else prefix_sum[i-1])
        self.prefix_sum = prefix_sum

    ## 2,   5,  3,  4
    ## 2,   7, 10, 14
    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sum[-1])
        l, r = 0, len(self.prefix_sum) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.prefix_sum[mid] == target:
                return mid
            if target < self.prefix_sum[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l


sol = Solution528([3, 14, 1, 7])
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())