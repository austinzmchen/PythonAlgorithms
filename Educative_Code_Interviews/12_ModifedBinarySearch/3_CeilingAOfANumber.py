# Problem Statement
# Given a sorted array of numbers and a target value, find the ceiling of the target. The ceiling is the smallest element in the array that is greater than or equal to the target.
# Examples:
# Input: arr = [1, 3, 8, 10, 15], target = 12
# Output: 15 (smallest number >= 12)

# Input: arr = [4, 6, 10], target = 6
# Output: 6 (equal counts as ceiling)

# Input: arr = [1, 3, 8, 10, 15], target = -1
# Output: 1 (smallest number >= -1)

# Input: arr = [1, 3, 8, 10, 15], target = 20
# Output: -1 (no ceiling exists)

def search_ceiling_of_a_number(arr, key):
  l, r = 0, len(arr) - 1
  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      return mid
    
    if key < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1

  if l >= len(arr):
    return -1
  return l


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))

main()


def search_floor_of_a_number(arr, key):
  l, r = 0, len(arr) - 1
  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      return mid

    if key < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1

  if r < 0:
    return -1
  return r


def main2():
  print(search_floor_of_a_number([4, 6, 10], 6))
  print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_floor_of_a_number([4, 6, 10], 17))
  print(search_floor_of_a_number([4, 6, 10], -1))

main2()
