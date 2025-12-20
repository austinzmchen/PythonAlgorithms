class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0
        self.cache = []  # Stores top-k (word, freq) pairs
        self.cache_size = 3  # Number of suggestions to cache

class AutoComplete:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, freq=1):
        """Insert word with given frequency"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.frequency = freq
        
        # Rebuild cache from root after insertion
        self._update_cache(self.root)
    
    def _update_cache(self, node):
        """Recursively update cache at each node"""
        suggestions = []
        
        # Collect all words from this subtree
        self._collect_words(node, "", suggestions)
        
        # Sort by frequency (desc) and keep top-k
        suggestions.sort(key=lambda x: x[1], reverse=True)
        node.cache = suggestions[:node.cache_size]
        
        # Recursively update children
        for child in node.children.values():
            self._update_cache(child)
    
    def _collect_words(self, node, prefix, suggestions):
        """Collect all words and frequencies from subtree"""
        if node.is_end:
            suggestions.append((prefix, node.frequency))
        
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, suggestions)
    
    def search(self, prefix):
        """Return top suggestions for given prefix using cache"""
        node = self.root
        
        # Navigate to prefix node
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Return cached suggestions
        return [prefix + word for word, freq in node.cache]
    

# Example usage
if __name__ == "__main__":
    ac = AutoComplete()
    
    # Insert words with frequencies
    words = [
        ("apple", 100),
        ("application", 80),
        ("apply", 60),
        ("app", 120),
        ("appreciate", 40),
        ("banana", 90),
        ("band", 70)
    ]
    
    for word, freq in words:
        ac.insert(word, freq)
    
    # Search with prefix
    print("Suggestions for 'app':")
    print(ac.search("app"))
    
    print("\nSuggestions for 'appl':")
    print(ac.search("appl"))
    
    print("\nSuggestions for 'ban':")
    print(ac.search("ban"))