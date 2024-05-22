def find_range(arr, key):
  l, r = 0, len(arr) - 1
  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      start, end = mid, mid
      for i in range(mid, len(arr)):
        if arr[i] == key:
          end = i
      for i in range(mid, -1, -1):
        if arr[i] == key:
          start = i
      return [start, end]

    if key < arr[mid]:
        r = mid - 1
    else:
      l = mid + 1

  return [-1, -1]


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()
