
def search_min_diff_element(arr, key):
  import sys
  min, res = sys.maxsize, 0

  l, r = 0, len(arr) - 1
  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      return arr[mid]
    
    diff = abs(arr[mid] - key)
    if diff < min:
      min = diff
      res = arr[mid]

    if key < arr[mid]:
      r = mid - 1
    else:
      l = mid + 1

  return res


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))

main()