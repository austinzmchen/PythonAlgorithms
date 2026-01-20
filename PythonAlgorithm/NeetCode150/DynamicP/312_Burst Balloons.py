class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        def recur(l, r):
            if l > r:
                return 0
            
            c = 0
            for i in range(l, r + 1):
                # Instead of thinking "which balloon to burst first", think "which balloon to burst last"!
                # When balloon i is the last to burst in range [l, r]:

                # All other balloons in [l, r] are already gone
                # Only boundaries l-1 and r+1 remain as neighbors
                
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += recur(l, i - 1) + recur(i + 1, r)
                c = max(c, coins)
            
            return c

        return recur(1, len(nums) - 2)