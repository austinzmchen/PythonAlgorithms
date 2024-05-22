
class Solution:
    
    def partition(self, s):
        res = []
        #  
        def dfs(idx, path):
            if idx == len(s):
                res.append(path)
                return
            for i in range(idx, len(s)):
                if isPal(idx, i):
                    dfs(i+1, path+[s[idx:i+1]])
        
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        dfs(0, [])
        return res
    
    
print(Solution().partition("aab"))