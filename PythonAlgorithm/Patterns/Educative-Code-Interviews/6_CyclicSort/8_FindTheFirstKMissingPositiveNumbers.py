"""
Statement
Given an unsorted integer array, arr, of size n and an integer k, 
find the first k missing positive integers from the array, ignoring all negative numbers and zeros.

If the array does not contain enough missing positive numbers, 
add the next consecutive positive integers, starting from the smallest number 
greater than the largest value in the array, until exactly k missing positive numbers have been found.

Return the list of the first k missing positive integers, sorted in ascending order.
"""

def find_first_k_missing_positive_1(nums, k):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and j < len(nums) and nums[i] != i + 1:
      if nums[j] == nums[i]:
        i += 1
      else:
        nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  res = []
  i = 0
  while k > 0:
    if i < len(nums):
      if nums[i] != i + 1:
        res.append(i + 1)
        k -= 1

      i += 1
    else:
      if i + 1 not in nums:
        res.append(i + 1)
        k -= 1
      i += 1

  return res


def find_first_k_missing_positive(nums, k):
  _set = set(nums)
  res = []
  
  v = 1
  while k > 0:
    if v not in _set:
      res.append(v)
      k -= 1
    v += 1
    
  return res
  
  
def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
