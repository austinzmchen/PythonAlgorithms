def find_subsets(nums):
  subsets = []
  subsets.append([])

  for num in nums:
    size = len(subsets)
    for i in range(size):
      ls = list(subsets[i])
      ls.append(num)
      subsets.append(ls)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
