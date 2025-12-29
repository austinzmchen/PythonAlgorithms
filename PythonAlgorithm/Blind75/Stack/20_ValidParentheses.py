class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        _map = {")": "(", "]": "[", "}": "{"}

        stack = deque()
        for c in s:
            print(f"{stack=}")

            if stack and _map.get(c) == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0