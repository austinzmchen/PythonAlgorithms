class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            curr = 0
            while n:
                d = n % 10
                n = n // 10
                curr += d * d

            if curr == 1:
                return True
            if curr in visited:
                return False
            
            n = curr
            visited.add(n)

        return False
    
print(Solution().isHappy(19))