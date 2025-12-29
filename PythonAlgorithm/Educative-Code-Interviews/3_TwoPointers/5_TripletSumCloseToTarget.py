# /*
# Problem Statement #
# Given an array of unsorted numbers and a target number, find a triplet in the array 
# whose sum is as close to the target number as possible, return the sum of the triplet. 
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:
# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

# Example 2:
# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

# Example 3:
# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.
#  */

def triplet_sum_close_to_target(arr, target_sum):
  import sys
  arr.sort()
  min_diff = sys.maxsize
  res = 0
  
  def search_pair(first, start_idx) -> int:
    nonlocal min_diff, res
    l, r = start_idx, len(arr) - 1

    while l < r:
      diff_abs = abs(target_sum - first - arr[l] - arr[r])
      if diff_abs < min_diff:
        min_diff = diff_abs
        res = first + arr[l] + arr[r]

      if arr[l] + arr[r] == target_sum - first:
        break # result found, handled above
      elif arr[l] + arr[r] < target_sum - first:
        l += 1
      else:
        r -= 1
        
  for i in range(0, len(arr) - 2):
    search_pair(arr[i], i + 1)
  return res


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()