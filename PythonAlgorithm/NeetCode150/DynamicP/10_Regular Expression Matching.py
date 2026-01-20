class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def recur(i: int, j: int) -> bool:
            # Pattern exhausted
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            # i can still not reach the end since j can be on the "*" char
            
            first_match = i < len(s) and p[j] == s[i] or p[j] == '.'
            
            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: Skip the pattern "c*" such as in s = "aab", p = "c*a*b"
                # Option 2: If first matches, consume one char from s and keep pattern
                return (recur(i, j + 2) or 
                        (first_match and recur(i + 1, j)))
            else:
                # Must match current character
                return first_match and recur(i + 1, j + 1)
            
        return recur(0, 0)
    

print(Solution().isMatch("aab", "c*a*b"))