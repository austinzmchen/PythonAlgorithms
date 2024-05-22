from functools import cache

class Node:
    def __init__(self, value, is_end=False):
        self.val = value
        self.map = {}
        self.is_end = is_end
        
        
class WordDictionary:

    def __init__(self):
        self.root = Node(None)
        

    def addWord(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.map:
                root.map[c] = Node(c)
            root = root.map[c]
        #
        root.is_end = True

        
    def search(self, word: str) -> bool:
        @cache
        def recur(node, idx) -> bool:
            if idx >= len(word):
                return node.is_end
            #
            c = word[idx]
            if c == '.':
                for child_n in node.map.values():
                    if recur(child_n, idx+1):
                      return True
                return False
            #
            if c in node.map:
                return recur(node.map[c], idx+1)
            return False
        #
        return recur(self.root, 0)
        
        
# wordDictionary = WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# print(wordDictionary.search("pad"))
# print(wordDictionary.search("bad"))
# print(wordDictionary.search(".ad"))
# print(wordDictionary.search("b.."))


wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
print(wordDictionary.search("a"))
print(wordDictionary.search(".at"))
wordDictionary.addWord("bat")
print(wordDictionary.search(".at"))
