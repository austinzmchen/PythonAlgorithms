from collections import defaultdict
from typing import List


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        #
        results = []
        #
        def recur(x, y, path, node):
            if node.is_word:
                results.append(path)
                node.is_word = False # remove duplicate if there are more than 1 path to reach the same word
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
                return
            #
            tmp = board[x][y]
            if not (n := node.children.get(tmp)):
                return
            path += tmp
            board[x][y] = "#" # serve as visited
            recur(x + 1, y, path, n)
            recur(x - 1, y, path, n)
            recur(x, y + 1, path, n)
            recur(x, y - 1, path, n)
            board[x][y] = tmp
            return
        #
        for i in range(len(board)):
            for j in range(len(board[i])):
                recur(i, j, "", trie.root)
        #
        return list(results)
    

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        #
        node.is_word = True
            
        
# r = Solution2().findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"])
# print(r)
r2 = Solution2().findWords([["a","a"]], ["aaa"])
print(r2)

## Time Limit Exceeded error
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_set = set(words)
        results = set()
        #
        def recur(x, y, path):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
                return
            if (tmp := board[x][y]) and tmp == "#":
                return
            path += tmp
            if path in word_set:
                results.add(path)
            #
            board[x][y] = "#"
            recur(x + 1, y, path)
            recur(x - 1, y, path)
            recur(x, y + 1, path)
            recur(x, y - 1, path)
            board[x][y] = tmp
            return
        #
        for i in range(len(board)):
            for j in range(len(board[i])):
                recur(i, j, "")
        #
        return list(results)
        