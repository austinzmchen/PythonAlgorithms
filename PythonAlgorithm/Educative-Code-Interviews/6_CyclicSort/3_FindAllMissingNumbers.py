
def find_missing_numbers(nums):
  res = []
  
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      # to avoid infinite swapping, check if the second num is at the right spot
      if nums[j] != j + 1:
        nums[i], nums[j] = nums[j], nums[i]
        continue
    i += 1

  for i, v in enumerate(nums):
    if v != i + 1:
      res.append(i + 1)
      
  return res


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()