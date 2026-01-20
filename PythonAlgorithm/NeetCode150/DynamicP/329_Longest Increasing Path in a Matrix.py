
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        from functools import lru_cache

        @lru_cache
        def recur(r, c, frm, curr_sum):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[r]):
                return 0
            
            if matrix[r][c] <= frm:
                return curr_sum
            
            return max(
                    recur(r + 1, c, matrix[r][c], curr_sum + 1),
                    recur(r - 1, c, matrix[r][c], curr_sum + 1),
                    recur(r, c + 1, matrix[r][c], curr_sum + 1),
                    recur(r, c - 1, matrix[r][c], curr_sum + 1))
        
        res = 1 # min answer
        import sys
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, recur(i, j, -sys.maxsize-1, 0))
        
        return res
    
    
print(Solution().longestIncreasingPath([[7,7,5],[2,4,6],[8,2,0]]))