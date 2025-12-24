from collections import defaultdict

class Solution79:
    def exist1(self, board: list[list[str]], word: str) -> bool:
        _dict = defaultdict(int)
        for x in range(len(board)):
            for y in range(len(board[x])):
                _dict[board[x][y]] += 1

        if _dict[word[0]] >= _dict[word[-1]]:
            word = word[::-1]
                
        def recur(x, y, idx):
            if idx == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
                return False
            if board[x][y] != word[idx]:
                return False
            #
            tmp = board[x][y]
            board[x][y] = ""
            found = recur(x-1, y, idx+1) or \
                recur(x, y-1, idx+1) or \
                recur(x+1, y, idx+1) or \
                recur(x, y+1, idx+1)
            board[x][y] = tmp
            return found

        for x in range(len(board)):
            for y in range(len(board[x])):
                if recur(x,y,0):
                    return True
        return False
    
    
    def exist(self, board: list[list[str]], word: str) -> bool:
        res = False
        from functools import lru_cache
        
        @lru_cache
        def recur(row, col, word_idx):
            if word_idx >= len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]):
                return False
            if word[word_idx] != board[row][col]:
                return False
            
            # must have, because you can not use the same char twice
            tmp = board[row][col] 
            board[row][col] = ""
            
            result = recur(row-1, col, word_idx + 1) or \
                    recur(row+1, col, word_idx + 1) or \
                    recur(row, col-1, word_idx + 1) or \
                    recur(row, col+1, word_idx + 1)
            
            board[row][col] = tmp
            return result

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                res = res or recur(r, c, 0)
        
        return res


# print(Solution79().exist([["A","B","C","E"],
#                           ["S","F","C","S"],
#                           ["A","D","E","E"]], "ABCB"))

print(Solution79().exist([["a"]], "a"))