class Solution7:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = x * -1

        s = []
        while x != 0:
            digit = x % 10
            s.append(digit)
            x = x // 10
            
        result = 0
        for n in s:
            result = result * 10 + n
        
        # solution expects  0 for overflow int
        if result > 2 ** 31 - 1:
            return 0
        
        if isNegative:
            result *= -1
            
        return result

if __name__ == "__main__":
    print(Solution7().reverse(197))