def remove_duplicates(arr):
  if len(arr) == 1: return 1

  left, right = 0, 1
  while right < len(arr):
    if arr[left] != arr[right]:
      arr[left + 1] = arr[right]
      left += 1
      right += 1
    else:
      right += 1
  return left + 1


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()