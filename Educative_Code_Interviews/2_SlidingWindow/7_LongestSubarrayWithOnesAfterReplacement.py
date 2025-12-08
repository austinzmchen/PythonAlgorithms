# /*
# Problem Statement #
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
# find the length of the longest contiguous subarray having all 1s.

# Example 1:
#
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s 
# having length 6.

# Example 2:
#
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s
# having length 9.
#
#  */

def length_of_longest_substring(arr, k):
  res = 0
  zero_count = 0
  win_s = 0

  for win_e, v in enumerate(arr):
    if v == 0: 
      zero_count += 1

    while zero_count > k:
      if arr[win_s] == 0:
        zero_count -= 1
      win_s += 1

    res = max(res, win_e - win_s + 1)
  return res


def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()