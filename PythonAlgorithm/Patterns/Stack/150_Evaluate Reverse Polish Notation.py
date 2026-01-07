from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()

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

            s.append(int(num))

        return s[0]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for t in tokens:
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a)) # truncates towards 0 == discard fractions
            else:
                stack.append(int(t))
        
        return stack.pop()


print(Solution().evalRPN(["2","1","+","3","*"]))
print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))