class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.recur(s, p, 0, 0)
    
    
    def recur(self, s: str, p: str, i, j) -> bool:
        if j == len(p):
            return i == len(s)
        #
        if j+1 < len(p) and p[j+1] == '*':
            if i < len(s) and (p[j] == '.' or s[i] == p[j]):
                return self.recur(s, p, i, j+2) or self.recur(s, p, i+1, j)
            else:
                return self.recur(s, p, i, j+2)
        else:
            if i < len(s) and (p[j] == '.' or s[i] == p[j]):
                return self.recur(s, p, i+1, j+1)
            return False