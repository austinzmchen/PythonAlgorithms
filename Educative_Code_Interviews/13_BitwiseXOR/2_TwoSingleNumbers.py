## not really using xor
def find_single_numbers(nums):
  _set = set()
  for num in nums:
    if num in _set:
      _set.remove(num)
    else:
      _set.add(num)

  return list(_set)


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
