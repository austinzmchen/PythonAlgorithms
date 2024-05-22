class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ls: [str] = []
        #
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        #
        while i >= 0 or j >= 0 or carry > 0:
            v1 = int(num1[i]) if i >= 0 else 0
            v2 = int(num2[j]) if j >= 0 else 0
            v = (v1 + v2 + carry)
            carry = v // 10
            v = v % 10
            ls.insert(0, str(v))
            #
            i -= 1
            j -= 1
        #
        return ''.join(ls)
            