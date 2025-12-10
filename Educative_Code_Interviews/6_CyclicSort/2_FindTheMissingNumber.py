# With 0 being a place holder, find the missing number from 
# the consecutive series of nums

def find_missing_number(nums):
  i = 0

  while i < len(nums):
    if nums[i] != 0 and nums[i] != i + 1:
      j = nums[i] - 1
      
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  for i, v in enumerate(nums):
    if v == 0:
      return i + 1

  pass


def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()