
class Solution79:
    def exist(self, board: List[List[str]], word: str) -> bool:
        _dict = defaultdict(int)
        for x in range(len(board)):
            for y in range(len(board[x])):
                _dict[board[x][y]] += 1
        #
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
        #
        for x in range(len(board)):
            for y in range(len(board[x])):
                if recur(x,y,0):
                    return True
        return False