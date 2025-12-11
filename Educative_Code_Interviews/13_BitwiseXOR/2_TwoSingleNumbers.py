
## not really using xor
def find_single_numbers(nums):
  seen = set()
  for num in nums:
    if num in seen:
      seen.remove(num)
    else:
      seen.add(num)

  return list(seen)


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + 
        str(find_single_numbers([2, 1, 3, 2])))

main()
