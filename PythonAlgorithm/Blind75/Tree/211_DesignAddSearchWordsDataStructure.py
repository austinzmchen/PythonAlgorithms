class Node:
    def __init__(self, value, is_end=False):
        self.val = value
        self.children = {}
        self.is_end = is_end
        
        
class WordDictionary:
    def __init__(self):
        self.root = Node(None)
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]

        node.is_end = True

        
    def search(self, word: str) -> bool:
        from functools import lru_cache
        
        @lru_cache
        def recur(node, i) -> bool:
            if i >= len(word):
                return node.is_end

            c = word[i]
            if c != '.':
                if c not in node.children:
                    return False
                return recur(node.children[c], i + 1)
            
            found = False                
            for cn in node.children.values():
                found = found or recur(cn, i + 1)
            return found

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
