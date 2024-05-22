def search_rotated_array(arr, key):
  l, r = 0, len(arr) - 1
  while l <= r:
    mid = l + (r - l) // 2
    if arr[mid] == key:
      return mid

    if arr[l] < arr[mid]:
      if key < arr[mid] and (found := binary_search(arr, key, l, mid - 1)) != -1:
        return found
      else:
        l = mid + 1
    else:
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


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
