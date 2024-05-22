def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      tmp = nums[i]
      nums[i] = nums[j]
      nums[j] = tmp
    else:
      i += 1
    
  return nums


def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
