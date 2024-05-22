def find_subsets(nums):
  nums.sort()
  subsets = []
  subsets.append([])
  size = 0

  for i in range(len(nums)):
    num = nums[i]
    
    start_idx = 0
    if i >= 1 and nums[i] == nums[i - 1]:
      start_idx = size
    size = len(subsets)

    for j in range(start_idx, size):
      ls = list(subsets[j])
      ls.append(num)
      subsets.append(ls)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
