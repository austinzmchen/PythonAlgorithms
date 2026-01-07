class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, idx = stack.pop()
                res = max(res, height * (i - idx))
                start = idx
                
            stack.append((h, start))
        
        for h, i in stack:
            res = max(res, h * (len(heights) - i))
            
        return res
    
    
print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([2,4]))