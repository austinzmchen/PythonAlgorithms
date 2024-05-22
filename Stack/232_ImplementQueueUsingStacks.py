class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp_s = []
        for i in range(len(self.stack)):
            temp_s.append(self.stack.pop(-1))
        #
        r = temp_s.pop(-1)
        for i in range(len(temp_s)):
            self.stack.append(temp_s.pop(-1))
        return r

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
