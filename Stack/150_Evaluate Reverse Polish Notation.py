from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()
        #
        for v in tokens:
            if v == '+':
                v2, v1 = s.pop(), s.pop()
                num = v1 + v2
            elif v == '-':
                v2, v1 = s.pop(), s.pop()
                num = v1 - v2
            elif v == '*':
                v2, v1 = s.pop(), s.pop()
                num = v1 * v2
            elif v == '/':
                v2, v1 = s.pop(), s.pop()
                num = v1 / v2
            else:
                num = v
            #
            s.append(int(num))
        #
        return s[0]
            