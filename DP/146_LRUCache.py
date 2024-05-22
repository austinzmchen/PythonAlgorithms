# dictionary in python 3.7+ is ordered
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self._dict = {}

    def get(self, key: int) -> int:
        if key not in self._dict:
            return -1
        #
        value = self._dict.pop(key)
        self._dict[key] = value
        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            self._dict.pop(key)
            self._dict[key] = value
            return
        #
        if self.size < self.cap:
            self.size += 1
        else:
            head_key = list(self._dict.keys())[0]
            del self._dict[head_key]
        #
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
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)