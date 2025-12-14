class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:
            
    def __init__(self):
        self.size = 100
        self.ls = [None] * self.size

    def put(self, key: int, value: int) -> None:
        if head := self.ls[key%self.size]:
            prev = None
            while head:
                if head.key == key:
                    head.value = value
                    return
                prev = head
                head = head.next
            prev.next = Node(key, value)
        else:
            self.ls[key%self.size] = Node(key, value)
        

    def get(self, key: int) -> int:
        if head := self.ls[key%self.size]:
            while head:
                if head.key == key:
                    return head.value
                head = head.next
        #
        return -1

    def remove(self, key: int) -> None:
        if head := self.ls[key%self.size]:
            if head.key == key:
                self.ls[key%self.size] = head.next
                return
            #
            prev = None
            while head:
                if head.key == key:
                    prev.next = head.next
                    return
                prev = head
                head = head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)