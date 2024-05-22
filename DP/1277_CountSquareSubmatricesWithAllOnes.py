from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def recur(row, col, step):
            for i in range(row, row+step):
                if i == len(matrix): return 0
                for j in range(col, col+step):
                    if j == len(matrix[i]): return 0
                    if matrix[i][j] == 0:
                        return 0
            #
            return 1 + recur(row, col, step+1)
        #
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if c := recur(i, j, 1):
                    count += c
        #
        return count
      
      
print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))