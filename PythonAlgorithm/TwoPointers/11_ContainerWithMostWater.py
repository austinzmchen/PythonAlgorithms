class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            m = (r - l) * min(height[l], height[r])
            if m > max_area:
                max_area = m
            #
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

