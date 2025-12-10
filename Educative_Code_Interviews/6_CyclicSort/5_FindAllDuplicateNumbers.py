
def find_all_duplicates(nums):
  res = []
  i = 0
  
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      
      if nums[j] != j + 1:
        nums[i], nums[j] = nums[j], nums[i]
        continue
    i += 1

  for i, v in enumerate(nums):
    if v != i + 1:
      res.append(v)
      
  return res


def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()