
class Dummy(str):
    def __lt__(self, other):
      return self + other > other + self
        
class Solution:
  
    def largestNumber(self, nums: List[int]) -> str:
      desc_strs = sorted(map(str, nums), key=Dummy)
      result = ''.join(desc_strs)
      return '0' if result[0] == '0' else result
    
    
    def largestNumber2(self, nums: List[int]) -> str:
      def cmp(x, y):
          return -1 if x + y > y + x else 1
      #
      from functools import cmp_to_key
      desc_strs = sorted(map(str, nums), key=cmp_to_key(cmp))
      result = ''.join(desc_strs)
      return '0' if result[0] == '0' else result  
    