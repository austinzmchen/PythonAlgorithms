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
        def recur(r, c, word_idx):
            if word_idx >= len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]):
                return False
            if word[word_idx] != board[r][c]:
                return False
            
            # must have, because you can not use the same char twice
            tmp = board[r][c] 
            board[r][c] = ""
            
            result = recur(r-1, c, word_idx + 1) or \
                    recur(r+1, c, word_idx + 1) or \
                    recur(r, c-1, word_idx + 1) or \
                    recur(r, c+1, word_idx + 1)
            
            board[r][c] = tmp
            return result

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                res = res or recur(r, c, 0)
        
        return res


    # Not working, why?
    def exist(self, board: list[list[str]], word: str) -> bool:
        from functools import lru_cache
        
        @lru_cache
        def recur(r, c, path):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]):
                return False
            if board[r][c] == "#":
                return False
            
            cell = board[r][c] 
            path += cell
            if path == word:
                return True
            
            board[r][c] = "#"
            found = recur(r - 1, c, path) or \
                    recur(r + 1, c, path) or \
                    recur(r, c - 1, path) or \
                    recur(r, c + 1, path)
            
            board[r][c] = cell
            return found

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if recur(r, c, ""):
                    return True
        return False
    

# print(Solution79().exist([["A","B","C","E"],
#                           ["S","F","C","S"],
#                           ["A","D","E","E"]], "ABCB"))

print(Solution79().exist([["a"]], "a"))