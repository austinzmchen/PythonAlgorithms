# Problem Statement
# Given a sorted array that has been rotated at some pivot point, find the index of a target value. The array was originally sorted in ascending order, then rotated.What is rotation?

# Original: [0, 1, 2, 4, 5, 6, 7]
# Rotated at index 4: [4, 5, 6, 7, 0, 1, 2]
# Examples:
# Input: arr = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4

# Input: arr = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1

# Input: arr = [1], target = 0
# Output: -1

# Input: arr = [10, 15, 1, 3, 8], target = 15
# Output: 1

def search_rotated_array(arr, key):
  l, r = 0, len(arr) - 1
  
  while l <= r:
    mid = l + (r - l) // 2
    if arr[mid] == key:
      return mid

    # check if left half is sorted
    if arr[l] < arr[mid]:
      # left half is sorted
      if key < arr[mid] and (found := binary_search(arr, key, l, mid - 1)) != -1:
        return found
      else:
        l = mid + 1
        
    else:
      # right half is sorted
      if key > arr[mid] and (found := binary_search(arr, key, mid + 1, r)) != -1:
        return found
      else:
        r = mid -1
        
  return -1


def binary_search(arr, key, start_idx, end_idx):
  l, r = start_idx, end_idx
  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      return mid

    if key < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1
  return -1


def search_rotated_array(arr, key):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        # Found target
        if arr[mid] == key:
            return mid
        
        # Determine which half is sorted
        if arr[l] <= arr[mid]:
            # Left half is sorted
            if arr[l] <= key < arr[mid]:
                # Target is in sorted left half
                r = mid - 1
            else:
                # Target is in right half
                l = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < key <= arr[r]:
                # Target is in sorted right half
                l = mid + 1
            else:
                # Target is in left half
                r = mid - 1
    
    return -1


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()