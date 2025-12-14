import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums = list(self.nums)
        def swap(x, y):
            tmp = nums[x]
            nums[x] = nums[y]
            nums[y] = tmp
        #
        for i in range(len(nums)):
            j = random.randint(0, len(nums) - 1)
            swap(i, j)
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()