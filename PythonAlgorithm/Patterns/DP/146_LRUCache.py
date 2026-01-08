
class LRUCache:
    # dictionary in python 3.7+ is ordered
    def __init__(self, capacity: int):
        self.cap = capacity
        self._dict = {}

    def get(self, key: int) -> int:
        if key not in self._dict:
            return -1

        v = self._dict.pop(key)
        self._dict[key] = v
        return v
        
    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            self._dict.pop(key)
            self._dict[key] = value
            return

        if len(self._dict) < self.cap:
            self._dict[key] = value
        else:
            k = next(iter(self._dict.keys()))
            self._dict.pop(k)
            self._dict[key] = value
            

class LRUCache2:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self._dict = {}
        self.linked_list = DoublyLinkedList()
        

    def get(self, key: int) -> int:
        if not (node := self._dict.get(key)):
            return -1
        #
        self.linked_list.remove(node)
        self.linked_list.append(node)
        self._dict[key] = node
        return node.val
        
    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if n := self._dict.get(key):
            self.linked_list.remove(n)
            self.linked_list.append(node)
            self._dict[key] = node
            return
        #
        self._dict[key] = node
        #
        if self.size < self.cap:
            self.linked_list.append(node)
            self.size += 1
        else:
            head = self.linked_list.head
            del self._dict[head.key]
            self.linked_list.remove(head)
            self.linked_list.append(node)
            

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        #
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
    
    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
    

class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val


# lru0 = LRUCache(2)
# lru0.put(1, 1); # cache is {1=1}
# lru0.put(2, 2); # cache is {1=1, 2=2}
# lru0.get(1);    # return 1
# lru0.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lru0.get(2);    # returns -1 (not found)
# lru0.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lru0.get(1);    # return -1 (not found)
# lru0.get(3);    # return 3
# lru0.get(4);    # return 4


lRUCache = LRUCache(2)
lRUCache.get(2)
lRUCache.put(2, 6)
lRUCache.get(1)
lRUCache.put(1, 5)
lRUCache.put(1, 2)
lRUCache.get(1)
lRUCache.get(2)