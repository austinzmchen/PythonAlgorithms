class Solution42:
    def trap(self, height: List[int]) -> int:
        new_heights = [0] * len(height)
        for i in range(0, len(height)):
            prev = 0 if i == 0 else new_heights[i - 1]
            new_heights[i] = max(prev, height[i])
        #
        res = 0
        for i in range(len(height) - 1, -1, -1):
            prev = 0 if i == len(height) - 1 else new_heights[i + 1]
            nh = max(prev, height[i])
            new_heights[i] = min(nh, new_heights[i])
            res += new_heights[i] - height[i]
        #
        return res
            