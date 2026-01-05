
def binary_search(arr, key):
  l, r = 0, len(arr) - 1
  
  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      return mid
    
    if arr[l] < arr[r]: ## ascending
      if key < arr[mid]:
        r = mid - 1
      else:
        l = mid + 1
    else:
      if key < arr[mid]:
        l = mid + 1
      else:
        r = mid - 1

  return -1


def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))

main()
