class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        _map = {")": "(", "]": "[", "}": "{"}

        stack = deque()
        for c in s:
            if stack and _map.get(c) == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0