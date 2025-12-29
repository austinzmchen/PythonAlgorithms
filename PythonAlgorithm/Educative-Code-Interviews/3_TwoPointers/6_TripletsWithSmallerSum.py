# /*
# Problem Statement #
# Given an array arr of unsorted numbers and a target sum, count all triplets in it 
# such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
# Write a function to return the count of such triplets.

# Example 1:
# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

# Example 2:
# Input: [-1, 4, 2, 1, 3], target=5
# Output: 4
# Explanation: There are four triplets whose sum is less than the target:
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
#
#  */

class TripletsWithSmallerSum:
  
  def __init__(self) -> None:
    self.count = 0

  def triplet_with_smaller_sum(self, arr, target):
    arr.sort()
    for i in range(0, len(arr) - 2):
      self.search_pair(arr, arr[i], i + 1, target)
    return self.count


  # -1, 1, 2, 3, 4
  def search_pair(self, arr, first, start_idx, target) -> int:
    for i in range(start_idx, len(arr) - 1):
      for j in range(i + 1, len(arr)):
        if first + arr[i] + arr[j] < target:
          self.count += 1


def triplet_with_smaller_sum_2(arr, target):
    arr.sort()
    res = 0
    
    def search_pair(first, start_idx) -> int:
      nonlocal res
      l, r = start_idx, len(arr) - 1
      
      while l < r:
        if first + arr[l] + arr[r] >= target:
          r -= 1
        else:
          # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
          # left and right to get a sum less than the target sum
          res += r - l # this only works when array has value increment by 1, such as [-1, 1, 2, 3, 4]
          l += 1
    
    for i in range(0, len(arr) - 2):
      search_pair(arr[i], i + 1)
    return res


def main():
  print(TripletsWithSmallerSum().triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(TripletsWithSmallerSum().triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
  
  print(triplet_with_smaller_sum_2([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum_2([-1, 4, 2, 1, 3], 5))


main()