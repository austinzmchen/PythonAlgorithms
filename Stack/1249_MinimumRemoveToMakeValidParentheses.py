class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        unwanted = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    unwanted.add(i)
        #
        for v in stack:
            unwanted.add(v)
        #
        str = ''
        for i, c in enumerate(s):
            if i not in unwanted:
                str += c
        #
        return str