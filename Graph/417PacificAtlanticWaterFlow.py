from typing import List

class Solution:
  
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        
        def recur(x, y, from_h, visited) -> str:
            if x < 0 or y < 0:
                return
            if x >= len(heights) or y >= len(heights[x]):
                return
            if (x, y) in visited or heights[x][y] < from_h:
                return
            
            visited.add((x,y))
            h = heights[x][y]
            recur(x-1, y, h, visited)
            recur(x, y-1, h, visited)
            recur(x+1, y, h, visited)
            recur(x, y+1, h, visited)
            return
         
        for x in range(len(heights)):
            recur(x, 0, heights[x][0], pac)
            recur(x, len(heights[0])-1, heights[x][-1], atl)
        for y in range(len(heights[0])):
            recur(0, y, heights[0][y], pac)
            recur(len(heights)-1, y, heights[-1][y], atl)

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
            
            

print(Solution().pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]))