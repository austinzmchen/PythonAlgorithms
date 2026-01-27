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
            
    
    # two pointers
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = 0, 0
        res = 0

        while l <= r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])
            
            if height[l] < height[r]:
                if max_l > height[l]:
                    res += max_l - height[l]

                l += 1
                
            else:
                if height[r] < max_r:
                    res += max_r - height[r]

                r -= 1
                
        return res
    

print(Solution42().trap([0,1,0,2,1,0,1,3,2,1,2,1]))