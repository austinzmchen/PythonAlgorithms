class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ls: [str] = []
        #
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        #
        while i >= 0 or j >= 0 or carry > 0:
            v1 = int(a[i]) if i >= 0 else 0
            v2 = int(b[j]) if j >= 0 else 0
            v = (v1 + v2 + carry)
            carry = v // 2
            v = v % 2
            ls.insert(0, str(v))
            #
            i -= 1
            j -= 1
        #
        return ''.join(ls)