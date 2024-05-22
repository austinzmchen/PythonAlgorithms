from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        _deque = deque()
        results = []
        for i, v in enumerate(nums):
            if _deque[0] <= i - k:
                _deque.popleft()
            #
            while len(_deque) > 0 and v > nums[_deque.peek()]:
                _deque.pop()
            _deque.append(i)
            #
            if i >= k - 1:
                results.append(nums[_deque[0]])
        #
        return results