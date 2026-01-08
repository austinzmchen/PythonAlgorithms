class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        size = rows * cols
        l, r = 0, size -1

        while l <= r:
            mid = (l + r) // 2
            x = mid // cols
            y = mid % cols

            if target == matrix[x][y]:
                return True
            
            if matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False