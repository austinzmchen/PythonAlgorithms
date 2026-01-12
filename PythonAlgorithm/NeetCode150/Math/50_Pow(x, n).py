class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1 / x, -n)

        # If n is even: x^n = (x^2)^(n/2)
        # If n is odd: x^n = x * x^(n-1)
        if n % 2 == 0:
            r = self.myPow(x, n // 2)
            return r * r
        else:
            return x * self.myPow(x, n - 1)

    # TLE
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        
        curr = x
        while n > 1:
            curr = curr * x
            n -= 1

        return curr