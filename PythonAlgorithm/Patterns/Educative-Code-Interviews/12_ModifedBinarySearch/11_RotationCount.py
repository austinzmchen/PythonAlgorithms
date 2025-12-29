"""
Rotation Count in Rotated Sorted Array

Problem: Given a rotated sorted array, find how many times it was rotated.
The rotation count equals the index of the minimum element.

Example:
    Input: [15, 18, 2, 3, 6, 12]
    Output: 2 (rotated 2 times, minimum element at index 2)
    
    Input: [7, 9, 11, 12, 5]
    Output: 4 (rotated 4 times, minimum element at index 4)
"""

# Key insight: The minimum element is the only element whose previous
# element is greater than it (break point in sorted order).

# find the smallest number index
def count_rotations(arr):
  l, r = 0, len(arr) - 1
  
  while l < r:
    print(f"{l=}, {r=}")
    mid = (l + r) // 2
    
    if arr[mid] > arr[mid + 1]:
      return mid + 1
    
    if arr[l] <= arr[mid]: # '=' is for when left is the mid, assuming no duplicates
      # left half is sorted, minimum is in right half
      l = mid + 1
    else:
      # right half is sorted
      r = mid

  return 0


def main():
  # print(count_rotations([10, 15, 1, 3, 8]))
  # print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))

main()