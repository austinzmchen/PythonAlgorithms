class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Result can have at most len(num1) + len(num2) digits
        res = [0] * (len(num1) + len(num2))
        
        # Reverse to make indexing easier (start from least significant digit)
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Multiply each digit of num1 with each digit of num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                carry = res[i + j] // 10
                
                res[i + j + 1] += carry
                res[i + j] %= 10  # Keep only last digit
        
        ss = ''.join(map(str, res[::-1])).lstrip("0")
        return ss if ss else "0"