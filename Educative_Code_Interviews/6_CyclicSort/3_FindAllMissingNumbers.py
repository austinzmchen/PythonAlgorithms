def find_missing_numbers(nums):
  missingNumbers = []
  
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
      missingNumbers.append(i + 1)
      
  return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()