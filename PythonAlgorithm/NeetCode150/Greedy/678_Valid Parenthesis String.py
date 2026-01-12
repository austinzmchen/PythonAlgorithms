
class Solution:
    
    def checkValidString(self, s: str) -> bool:
        def recur(i, open_count):
            if i >= len(s):
                return open_count == 0
            
            # If open_count goes negative, invalid
            if open_count < 0:
                return False
            
            if s[i] == "(":
                return recur(i + 1, open_count + 1)
            if s[i] == ")":
                return recur(i + 1, open_count - 1)
            
            # try all 3 possibility, match ( or ) or ""
            return recur(i + 1, open_count + 1) or \
                    recur(i + 1, open_count - 1) or \
                    recur(i + 1, open_count)
        return recur(0, 0)
    
    
    # Not working, does not handle "()()"
    def checkValidString(self, s: str) -> bool:
        def recur(l, r):
            if l > r:
                return True
            if l == r:
                return s[l] == s[r] == "*"
            
            if s[l] == "*" and s[r] in ["*", ")"]:
                # treat * as "(" or as ""
                return recur(l + 1, r - 1) or \
                        recur(l + 1, r)
            
            if s[r] == "*" and s[l] in ["*", "("]:
                # treat * as ")" or as ""
                return recur(l + 1, r - 1) or \
                        recur(l, r - 1)

            return s[l] == "(" and s[r] == ")" and recur(l + 1, r - 1)

        return recur(0, len(s) - 1)
    
    
    # Two-Pass Greedy (Forward & Backward)
    #   This elegant approach checks balance in both directions:
    
    def checkValidString(s: str) -> bool:
        # Forward pass: treat '*' as '(' when needed
        balance = 0
        for char in s:
            if char == '(' or char == '*':
                balance += 1
            else:  # char == ')'
                balance -= 1
            
            if balance < 0:
                return False
        
        # Backward pass: treat '*' as ')' when needed
        balance = 0
        for char in reversed(s):
            if char == ')' or char == '*':
                balance += 1
            else:  # char == '('
                balance -= 1
            
            if balance < 0:
                return False
        
        return True
    

print(Solution().checkValidString("(*)"))
print(Solution().checkValidString("(*))"))    
print(Solution().checkValidString("()()")) # should be True