def find_first_smallest_missing_positive(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and j < len(nums) and \
            nums[i] != i + 1:

      if nums[j] == nums[i]:
        i += 1
      else:
        nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  for i in range(len(nums)):
    if nums[i] != i + 1:
      return i + 1
  pass


def main():
  print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()
