class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # The algorithm maintains a stack of bars in increasing height order. 
        # When it encounters a shorter bar, it knows that previous taller bars can't extend beyond this point, 
        # so it calculates their maximum rectangle areas.
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, height * (i - idx))
                
                # current bar h can extend backward to where that taller bar started
                start = idx
                
            stack.append((start, h))
        
        # stack stores at this point
        # [(0, 1), (2, 2), (5, 3)]
        
        # left over increasing tiles 
        for idx, h in stack:
            # len(heights) is like `i` above
            res = max(res, h * (len(heights) - idx))
            
        return res
    
    
print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([2,4]))