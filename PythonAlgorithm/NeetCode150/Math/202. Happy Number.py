class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            v = 0
            while n:
                d = n % 10
                n = n // 10
                v += d * d

            if v == 1:
                return True
            if v in visited:
                return False
            
            n = v
            visited.add(n)

        return False
    
print(Solution().isHappy(19))