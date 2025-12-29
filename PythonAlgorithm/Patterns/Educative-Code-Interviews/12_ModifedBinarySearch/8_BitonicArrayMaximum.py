# Problem Statement
# A bitonic array is an array that first increases, then decreases. 
# Find the maximum element (the peak) in a bitonic array.
# Definition: A bitonic array has these properties:
#
# Elements first increase: arr[0] < arr[1] < ... < arr[k]
# Then decrease: arr[k] > arr[k+1] > ... > arr[n-1]
# arr[k] is the maximum (the peak)

def find_max_in_bitonic_array(arr):
  l, r = 0, len(arr) - 1
  
  while l < r:
    mid = r + (l - r) // 2
    
    if arr[mid] < arr[mid + 1]:
      l = mid + 1
    else:
      r = mid

  return arr[l]


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))

main()