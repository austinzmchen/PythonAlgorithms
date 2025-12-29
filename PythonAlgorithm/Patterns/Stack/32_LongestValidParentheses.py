class Solution:
    
    def longestValidParentheses(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack
        
        The workflow of the solution is as below.
        - Scan the string from beginning to end.
        - If current character is '(',
          push its index to the stack. If current character is ')' and the
          character at the index of the top of stack is '(', we just find a
          matching pair so pop from the stack. Otherwise, we push the index of
          ')' to the stack.
        - After the scan is done, the stack will only
          contain the indices of characters which cannot be matched. Then
          let's use the opposite side - substring between adjacent indices
          should be valid parentheses.
        - If the stack is empty, the whole input
          string is valid. Otherwise, we can scan the stack to get longest
          valid substring as described in step 3.
        """
        stack = []
        for i, c in enumerate(s):
            if len(stack) > 0 and s[stack[-1]] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(i)
        #
        if len(stack) == 0:
            return len(s)
        #
        longest = 0
        n = len(s)
        while len(stack) > 0:
            m = stack.pop()
            longest = max(longest, n - m - 1)
            n = m
        longest = max(longest, n)
        #
        return longest