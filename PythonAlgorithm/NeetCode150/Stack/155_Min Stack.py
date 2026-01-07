from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            _min = min(val, self.getMin())
            self.stack.append((val, _min))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        t = self.stack[-1]
        return t[0]

    def getMin(self) -> int:
        t = self.stack[-1]
        return t[1]


stack = MinStack()
stack.push(5)     # stack: [(5, 5)], _min: 5
stack.push(2)     # stack: [(5, 5), (2, 2)], _min: 2
stack.push(3)     # stack: [(5, 5), (2, 2), (3, 2)], _min: 2
stack.pop()       # stack: [(5, 5), (2, 2)], _min: 2 ✓ (still correct)
stack.pop()       # stack: [(5, 5)], _min: 2 ❌ (WRONG! Should be 5)
print(stack.getMin())    # Returns 2, but should return 5!