
class Solution:
    
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