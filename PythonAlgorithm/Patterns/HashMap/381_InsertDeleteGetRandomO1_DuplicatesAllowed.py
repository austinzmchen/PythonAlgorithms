from collections import defaultdict
import random


class RandomizedCollection381:

    def __init__(self):
        self.dict = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        res = val not in self.dict
        self.list.append(val)
        self.dict[val].add(len(self.list) - 1)
        return res

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # 
        if val == self.list[-1]:
            self.dict[val].remove(len(self.list)-1) # remove value from set is O(1)
            self.list.pop()
            if len(self.dict[val]) == 0:
                del self.dict[val]
            return True
        #
        val_idx_0 = self.dict[val].pop()
        if len(self.dict[val]) == 0:
            del self.dict[val]
        last = self.list[-1]
        #
        self.list[val_idx_0] = last
        self.dict[last].remove(len(self.list)-1) # remove value from set is O(1)
        self.dict[last].add(val_idx_0)
        #
        self.list.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.list) - 1)
        return self.list[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection381()
param_1 = obj.insert(4)
param_1 = obj.insert(3)
param_1 = obj.insert(4)
param_1 = obj.insert(2)
param_1 = obj.insert(4)

param_2 = obj.remove(4)
param_2 = obj.remove(3)
param_2 = obj.remove(4)
param_2 = obj.remove(4)


obj2 = RandomizedCollection381()
param_1 = obj2.insert(10)
param_1 = obj2.insert(10)
param_1 = obj2.insert(20)
param_1 = obj2.insert(20)
param_1 = obj2.insert(30)
param_1 = obj2.insert(30)

param_2 = obj2.remove(10)
param_2 = obj2.remove(20)
param_2 = obj2.remove(20)
param_2 = obj2.remove(10)
param_2 = obj2.remove(30)
param_2 = obj2.remove(40)
param_2 = obj2.remove(30)
param_2 = obj2.remove(30)


obj3 = RandomizedCollection381()
param_1 = obj3.insert(1)
param_1 = obj3.insert(1)
param_1 = obj3.insert(2)
param_1 = obj3.insert(2)
param_1 = obj3.insert(2)

param_2 = obj3.remove(1)
param_2 = obj3.remove(1)
param_2 = obj3.remove(2)
param_2 = obj3.insert(1)
param_2 = obj3.remove(2)