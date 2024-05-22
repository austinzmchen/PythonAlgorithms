def dutch_flag_sort(arr):
  l, r = 0, len(arr) - 1
  while l < r: 
    if arr[l] > arr[r]:
      tmp = arr[l]
      arr[l] = arr[r]
      arr[r] = tmp
    
    if arr[l] == 1 and arr[r] == 1:
      break
    if arr[l] == 0:
      l += 1
    if arr[r] == 2:
      r -= 1


def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)


main()