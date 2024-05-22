class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    queue.append((r, c))
        #
        while queue:
            r, c = queue.pop(0)
            for ri in range(len(matrix)):
                matrix[ri][c] = 0
            for ci in range(len(matrix[r])):
                matrix[r][ci] = 0
        
        return