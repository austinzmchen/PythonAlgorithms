class Solution:
    def hammingWeight(self, n: int) -> int:
        m = n
        count = 0
        while m > 0:
            if m & 1:
                count += 1
            m = m >> 1
        #
        return count