import hashlib
from bisect import bisect_right

class ConsistentHash:
    """
    Consistent Hashing implementation using SHA-1 hash function.
    Supports virtual nodes to improve distribution.
    """
    
    def __init__(self, nodes:list[str]=None, virtual_nodes=150):
        """
        Initialize consistent hash ring.
        
        Args:
            nodes: List of server/node names
            virtual_nodes: Number of virtual nodes per physical node
        """
        self.virtual_nodes = virtual_nodes
        
        # these 2 vars create the ring structure
        self.ring = {}  # hash -> node mapping
        self.sorted_nodes = []  # sorted hash values of nodes
        
        if nodes:
            for node in nodes:
                self.add_node(node)
    
    def _hash(self, key:str):
        """Generate SHA-1 hash and convert to integer."""
        hash_str = hashlib.sha1(key.encode('utf-8')).hexdigest() # 40 chars hexadecimal string
        return int(hash_str, 16) # convert to int from hex string
    
    def add_node(self, node:str):
        """Add a node with virtual nodes to the ring."""
        for i in range(self.virtual_nodes):
            virtual_key = f"{node}:{i}"
            hash_val = self._hash(virtual_key)
            self.ring[hash_val] = node
            self.sorted_nodes.append(hash_val)
        
        self.sorted_nodes.sort()
        print(f"Added node '{node}' with {self.virtual_nodes} virtual nodes")
    
    def remove_node(self, node:str):
        """Remove a node and its virtual nodes from the ring."""
        for i in range(self.virtual_nodes):
            virtual_key = f"{node}:{i}"
            hash_val = self._hash(virtual_key)
            if hash_val in self.ring:
                del self.ring[hash_val]
                self.sorted_nodes.remove(hash_val)
        
        print(f"Removed node '{node}'")
    
    def get_node(self, key:str) -> str:
        """
        Get the node (actual node name, not virtual node name) responsible for a given key.
        Uses clockwise search on the ring.
        """
        if not self.ring:
            return None
        
        hash_val = self._hash(key)
        
        # Find the first node clockwise from the hash position
        #   bisection search, if not found, return the next idx
        idx = bisect_right(self.sorted_nodes, hash_val)
        
        # Wrap around if we're past the end
        if idx == len(self.sorted_nodes):
            idx = 0
        
        return self.ring[self.sorted_nodes[idx]]
    
    def get_nodes(self, key, n=1):
        """
        For Replication in Chapter 6
        
        Get n nodes responsible for a key (for replication).
        Returns unique physical nodes.
        """
        if not self.ring or n <= 0:
            return []
        
        hash_val = self._hash(key)
        idx = bisect_right(self.sorted_nodes, hash_val)
        
        nodes = []
        seen = set() # since there are virtual nodes, remove duplicates
        
        # Walk clockwise around the ring
        for i in range(len(self.sorted_nodes)):
            # so idx wraps around the ring
            pos = (idx + i) % len(self.sorted_nodes)
            
            node = self.ring[self.sorted_nodes[pos]]
            
            if node not in seen:
                nodes.append(node)
                seen.add(node)
                
                if len(nodes) == n:
                    break
        
        return nodes
    
    def distribution(self, keys):
        """Analyze key distribution across nodes."""
        dist = {}
        for key in keys:
            node = self.get_node(key)
            dist[node] = dist.get(node, 0) + 1
        return dist


# Example usage and testing
if __name__ == "__main__":
    print("=== Consistent Hashing Demo ===\n")
    
    # Create hash ring with 3 servers
    ch = ConsistentHash(
        nodes=["server1", "server2", "server3"],
        virtual_nodes=150
    )
    
    print("\n--- Testing Key Assignment ---")
    keys = ["user:1001", "user:1002", "user:1003", "session:abc", "cache:xyz"]
    
    for key in keys:
        node = ch.get_node(key)
        print(f"Key '{key}' -> {node}")
    
    print("\n--- Testing Replication (3 replicas) ---")
    key = "important_data"
    replicas = ch.get_nodes(key, n=3)
    print(f"Key '{key}' replicated to: {replicas}")
    
    print("\n--- Adding New Server ---")
    ch.add_node("server4")
    
    print("\nKey assignments after adding server4:")
    for key in keys:
        node = ch.get_node(key)
        print(f"Key '{key}' -> {node}")
    
    print("\n--- Removing Server ---")
    ch.remove_node("server2")
    
    print("\nKey assignments after removing server2:")
    for key in keys:
        node = ch.get_node(key)
        print(f"Key '{key}' -> {node}")
    
    print("\n--- Distribution Analysis ---")
    # Generate 10000 test keys
    test_keys = [f"key:{i}" for i in range(10000)]
    dist = ch.distribution(test_keys)
    
    print(f"\nDistribution of {len(test_keys)} keys:")
    for node, count in sorted(dist.items()):
        percentage = (count / len(test_keys)) * 100
        print(f"{node}: {count} keys ({percentage:.2f}%)")