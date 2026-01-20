class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1

        while i >= 0 and carry == 1:
            n = digits[i]
            if n < 9:
                digits[i] = n + 1
                carry = 0
            else:
                digits[i] = 0
                carry = 1
                i -= 1

        if i < 0 and carry == 1:
            digits.insert(0, 1)
        
        return digits
    
    
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        res = []
        
        while i >= 0:
            n = digits[i]
            n += carry
            
            carry = n // 10
            n = n % 10
            
            res.insert(0, n)
            i -= 1

        if i < 0 and carry == 1:
            res.insert(0, 1)
        
        return res