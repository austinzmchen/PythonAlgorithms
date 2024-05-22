def find_missing_number(nums):
  i = 0

  while i < len(nums):
    if nums[i] != 0 and nums[i] != i + 1:
      j = nums[i] - 1
      tmp = nums[i]
      nums[i] = nums[j]
      nums[j] = tmp
    else:
      i += 1

  for i in range(len(nums)):
    if nums[i] == 0:
      return i + 1

  pass


def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()