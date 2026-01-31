
class Solution:
    
    # need to traverse char by char and check if intervals of chars are palindrom
    def partition(self, s):
        res = []
        
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def recur(i, path):
            # When we've processed the entire string, we've found a valid partition.
            if i == len(s):
                res.append(path)
                return
            
            # - Try every possible end position `j` starting from `i`
            # - If `s[i:j+1]` is a palindrome, add it to the path
            # - Recursively partition the remaining substring starting at `j+1`
            for j in range(i, len(s)):
                if is_pal(i, j):
                    ss = s[i:j+1]
                    # only move on to the next char if pal found,
                    recur(j + 1, path + [ss])
            
        recur(0, [])
        return res
    
    
print(Solution().partition("aab"))