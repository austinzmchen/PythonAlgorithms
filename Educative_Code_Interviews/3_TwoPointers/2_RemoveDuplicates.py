# /*
# Problem Statement #
# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
# after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].
#  */

def remove_duplicates(arr):
  if len(arr) == 1: return 1

  left, right = 0, 1
  while right < len(arr):
    if arr[left] == arr[right]:
      right += 1
    else:
      arr[left + 1] = arr[right]
      left += 1
      right += 1
  return left + 1


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()