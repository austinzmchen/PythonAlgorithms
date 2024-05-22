def find_permutations(nums):
  perms = []
  perms.append([])
  result = []

  for num in nums:
    for i in range(len(perms)):
      for j in range(len(perms[i]) + 1): # +1 because insert before or after a num
        ls = list(perms[i]) # new list
        ls.insert(j, num)
        perms.append(ls)

        if len(nums) == len(ls):
          result.append(ls)

  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
