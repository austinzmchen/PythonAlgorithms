from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        temp_q, self.q = self.q.copy(), []
        self.q.append(x)
        self.q.extend(temp_q)

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.top())