from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)]  # 2d array
        # board = [["."] * n] * n # this creates an array of (array of same reference)
        results = []
        #
        def recur(row):
            if row == n:
                results.append(list(map(lambda x: ''.join(x), board)))
                return
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    recur(row+1)
                    board[row][col] = "."
        # check if valid if adding queen at (row, col)
        def is_valid(row, col):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == "Q" and \
                      (i + j == row + col or i - j == row - col or j == col):
                        return False
            return True
        #
        recur(0)
        return results
      

print(Solution().solveNQueens(4))