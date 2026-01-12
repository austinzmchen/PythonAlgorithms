from typing import List

class Solution:
    
    # start from the boundary and mark O as -
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        def recur(r: int, c: int) -> None:
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            # Skip if already processed or is a wall
            if board[r][c] in ["-", "X"]:
                return
            
            board[r][c] = '-' # Mark this cell as safe (connected to border)
            recur(r - 1, c)
            recur(r + 1, c)
            recur(r, c - 1)
            recur(r, c + 1)
            
        # Check first and last columns
        for r in range(len(board)):
            if board[r][0] == 'O':
                recur(r, 0)
            if board[r][-1] == 'O':
                recur(r, len(board[r]) - 1)
        
        # Check first and last rows
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                recur(0, c)    
            if board[-1][c] == 'O':
                recur(len(board) - 1, c)
        
        # Restore marked cells and flip surrounded regions
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '-':
                    board[r][c] = 'O'
                elif cell == 'O':
                    board[r][c] = 'X'


# Example usage
solution = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
solution.solve(board)
print(board)
# Output: [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]