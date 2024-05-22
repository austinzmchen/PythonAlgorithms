import sys


def search_min_diff_element(arr, key):
  l, r = 0, len(arr) - 1
  _min, _min_num = sys.maxsize, 0

  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      return arr[mid]
    
    if abs(arr[mid] - key) < _min:
      _min = abs(arr[mid] - key)
      _min_num = arr[mid]

    if key < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1

  return _min_num


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()
