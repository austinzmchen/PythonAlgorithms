from typing import List

class Solution:
  
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        
        # start from the shores and proceed if the curr height is higher or equal
        def recur(x, y, from_h, visited) -> str:
            if x < 0 or y < 0 or x >= len(heights) or y >= len(heights[x]):
                return
            
            h = heights[x][y]
            if (x, y) in visited or h < from_h: 
                return
                        
            visited.add((x,y))
            recur(x - 1, y, h, visited)
            recur(x, y - 1, h, visited)
            recur(x + 1, y, h, visited)
            recur(x, y + 1, h, visited)
        
        # going from left shore
        for row in range(len(heights)):
            recur(row, 0, heights[row][0], pac)
        # going from top shore
        for col in range(len(heights[0])):
            recur(0, col, heights[0][col], pac)
        # going from right shore
        for row in range(len(heights)):
            recur(row, len(heights[0])-1, heights[row][-1], atl)
        # going from bottom shore
        for col in range(len(heights[0])):
            recur(len(heights)-1, col, heights[-1][col], atl)
        
        return pac & atl
      
      
    # TLE
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        import sys
        cache = {}
        
        def recur(x, y, from_h) -> str:
            if x < 0 or y < 0:
                return 'pacific'
            if x >= len(heights) or y >= len(heights[x]):
                return 'atlantic'
            if from_h != sys.maxsize and heights[x][y] > from_h:
                return 'none'
            
            if (x, y) in cache:
                return cache[(x, y)]
            
            h = heights[x][y]
            heights[x][y] = sys.maxsize
            neighbors = {recur(x-1, y, h),
                        recur(x, y-1, h),
                        recur(x+1, y, h),
                        recur(x, y+1, h)}
            
            heights[x][y] = h
            #
            if 'both' in neighbors:
                r = 'both'
            elif 'pacific' in neighbors and 'atlantic' in neighbors:
                r = 'both'
            elif 'pacific' in neighbors:
                r = 'pacific'
            elif 'atlantic' in neighbors:
                r = 'atlantic'
            else:
                r = 'none'
            return r
          
            
        res = []
        for x in range(len(heights)):
            for y in range(len(heights[x])):
                r = recur(x, y, sys.maxsize)
                cache[(x, y)] = r
                if 'both' == r:
                    res.append([x, y])
        #
        return res
            
    
    # Not working!, for following example
    # [1,2,3],
    # [8,9,4],
    # [7,6,5]
    #
    def pacificAtlantic_0(self, heights: List[List[int]]) -> List[List[int]]:
        from functools import lru_cache

        @lru_cache
        def recur(r, c, flag:str) -> bool:
            if flag == "p" and (r == 0 or c == 0):
                return True
            if flag == "a" and (r == len(heights) - 1 or c == len(heights[r]) - 1):
                return True
            
            curr = heights[r][c]
            if flag == "p":
                if curr < heights[r-1][c] and curr < heights[r][c-1]:
                    return False
                else:
                    return recur(r-1, c, "p") or recur(r, c-1, "p")
            else:
                if curr < heights[r+1][c] and curr < heights[r][c+1]:
                    return False
                else:
                    return recur(r+1, c, "a") or recur(r, c+1, "a")
                
        res = []
        for i_r, row in enumerate(heights):
            for i_c, cell in enumerate(row):
                if recur(i_r, i_c, "p") and recur(i_r, i_c, "a"):
                    res.append([i_r, i_c])
        
        return res
    
    
print(Solution().pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]))