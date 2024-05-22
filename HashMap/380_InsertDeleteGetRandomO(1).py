import random


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dict = {} # track value and index

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        #
        # swap the last one with the to-be-deleted one, then delete
        # this way, no need to move position for every item
        last = self.list[-1]
        val_idx = self.dict[val]
        self.list[val_idx] = last
        self.dict[last] = val_idx
        #
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.list) - 1)
        return self.list[idx]

