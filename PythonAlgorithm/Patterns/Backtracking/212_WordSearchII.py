from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]

        node.is_end = True
        
        
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = []

        def recur(x, y, path, node):
            if node.is_word:
                res.append(path)
                node.is_word = False # remove duplicate if there are more than 1 path to reach the same word
                
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
                return

            cell = board[x][y]
            if not (n := node.children.get(cell)):
                return
            path += cell
            
            board[x][y] = "#" # serve as visited
            recur(x + 1, y, path, n)
            recur(x - 1, y, path, n)
            recur(x, y + 1, path, n)
            recur(x, y - 1, path, n)
            board[x][y] = cell
            return

        for i in range(len(board)):
            for j in range(len(board[i])):
                recur(i, j, "", trie.root)

        return list(res)
            
        
# r = Solution2().findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"])
# print(r)
r2 = Solution2().findWords([["a","a"]], ["aaa"])
print(r2)

## Time Limit Exceeded error
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = set(words)
        res = set()

        def recur(x, y, path):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
                return
            
            if (cell := board[x][y]) and cell == "#":
                return
            
            path += cell
            if path in words:
                if path not in res: # for case of words ["oa", "oaa"]
                    res.add(path)

            board[x][y] = "#"
            recur(x + 1, y, path)
            recur(x - 1, y, path)
            recur(x, y + 1, path)
            recur(x, y - 1, path)
            board[x][y] = cell
            return

        for i in range(len(board)):
            for j in range(len(board[i])):
                recur(i, j, "")

        return list(res)
        