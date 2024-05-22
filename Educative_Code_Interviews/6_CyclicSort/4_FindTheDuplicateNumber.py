def find_duplicate(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[j] != j + 1:
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
      else:
        i += 1
    else:
      i += 1

  for i in range(0, len(nums)):
    if nums[i] != i + 1:
      return nums[i]
      
  pass


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()