def find_corrupt_numbers(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[j] == nums[i]:
        i += 1
      else:
        nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  for i in range(len(nums)):
    if nums[i] != i + 1:
      return [nums[i], i + 1]
      
  return [-1, -1]


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()
