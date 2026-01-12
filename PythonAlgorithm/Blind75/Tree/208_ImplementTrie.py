class Node:
    def __init__(self, value, is_end=False):
        self.val = value
        self.children = {}
        self.is_end = is_end
        
        
class Trie:
    def __init__(self):
        self.root = Node(None)


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]

        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.is_end
    

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        # return not node.is_end
        return True


class Trie1:
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