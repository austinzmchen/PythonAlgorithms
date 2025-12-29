import math

# https://www.youtube.com/watch?v=W9SIlE2jhBQ
class Solution:
    def find_kth_permutation(self, v, k, result):
        if not v or len(v) == 0:
            return

        n = len(v)
        # factorial is number of permutations starting with first digit,
        # selected is the number of digits in permutation
        _f = math.factorial(n - 1)
        selected = (k - 1) // _f

        # Get the first digit from selected array
        result += str(v[selected])
        del v[selected] # so that index shifts
        k = k - (_f * selected)
        
        # Recursively calling itself
        self.find_kth_permutation(v, k, result)


    def getPermutation(self, n: int, k: int) -> str:
        v = list(range(1, n + 1))
        result = []
        self.find_kth_permutation(v, k, result)
        return ''.join(result)
      

print(Solution().getPermutation(3,3))