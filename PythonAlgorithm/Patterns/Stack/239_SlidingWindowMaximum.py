from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        results = []
        
        for i, n in enumerate(nums):
            # pop indexes less than the window
            if deq and deq[0][1] <= i - k:
                deq.popleft()

            # pop smaller n, latest n appended to right
            while deq and deq[-1][0] < n:
                deq.pop()
            deq.append((n, i))

            if i >= k - 1:
                # max n at left
                results.append(deq[0][0])

        return results
    
    
    # TLE
    def maxSlidingWindow0(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = [] # not optimal
        res = []

        for r, n in enumerate(nums):
            window.append(n)

            if r >= k:
                window.remove(nums[l])
                l += 1
            
            if r >= k - 1:
                res.append(max(window))
        
        return res
    
    
print(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))