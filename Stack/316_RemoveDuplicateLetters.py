class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_indexes = {}
        for i, c in enumerate(s):
            last_indexes[c] = i
        #
        stack = []
        for i, c in enumerate(s):
            if c in stack: # can use a set to check membership
                continue
            while len(stack) > 0 and c < stack[-1] and last_indexes[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        #
        return "".join(stack)