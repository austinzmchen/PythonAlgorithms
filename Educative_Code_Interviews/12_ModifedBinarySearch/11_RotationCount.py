# find the smallest number index
def count_rotations(arr):
  l, r = 0, len(arr) - 1
  while l < r:
    mid = l + (r - l) // 2
    if arr[mid] > arr[mid + 1]:
      return mid + 1
    
    if arr[l] <= arr[mid]: # '=' is for when left is the mid, assuming no duplicates
      l = mid + 1
    else:
      r = mid

  return 0


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()
