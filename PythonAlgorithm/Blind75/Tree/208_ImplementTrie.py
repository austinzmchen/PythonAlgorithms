class Node1:
    def __init__(self, value, is_end=False):
        self.val = value
        self.map = {}
        self.is_end = is_end
        
        
class Trie1:

    def __init__(self):
        self.root = Node1(None)

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.map:
                root.map[c] = Node1(c)
            root = root.map[c]

        root.is_end = True
        

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root.map:
                return False
            root = root.map[c]
        #
        return root.is_end
    

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.map:
                return False
            root = root.map[c]
        #
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Node:
    def __init__(self, val=""):
        # self.val = val # this impl does not seem to need val
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = Node("")
        

    def insert(self, word: str) -> None:
        def recur(idx, node):
            if idx == len(word):
                node.is_end = True
                return
            if not node:
                return False
            
            c = word[idx]
            if child := node.children.get(c):
                recur(idx + 1, child)
            else:
                new_node = Node(c)
                node.children[c] = new_node

                # print(f"{c=}, {idx=}")
                recur(idx + 1, new_node)
        
        recur(0, self.root)
        

    def search(self, word: str) -> bool:
        def recur(idx, node):
            if idx == len(word):
                if node and node.is_end:
                    return True
                return False
            
            if not node:
                return False
            
            c = word[idx]
            return recur(idx + 1, node.children.get(c))
        
        return recur(0, self.root)


    def startsWith(self, prefix: str) -> bool:
        def recur(idx, node):
            if idx == len(prefix):
                # not checking is_end, imagine adding words "apple", then "app", 
                #   startsWith "app" should still be True
                if node:
                    return True
                return False
            
            if not node:
                return False

            return recur(idx + 1, node.children.get(prefix[idx]))
        return recur(0, self.root)


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))