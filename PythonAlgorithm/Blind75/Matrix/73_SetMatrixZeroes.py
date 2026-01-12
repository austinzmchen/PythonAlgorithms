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

        while queue:
            r, c = queue.pop(0)
            for ri in range(len(matrix)):
                matrix[ri][c] = 0
            for ci in range(len(matrix[r])):
                matrix[r][ci] = 0
        
        return
    
    
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_set = set()
        c_set = set()

        for i_r, row in enumerate(matrix):
            for i_c, cell in enumerate(row):
                if cell == 0:
                    r_set.add(i_r)
                    c_set.add(i_c)
        
        for i_r, row in enumerate(matrix):
            for i_c, cell in enumerate(row):
                if i_r in r_set or i_c in c_set:
                    row[i_c] = 0

        return