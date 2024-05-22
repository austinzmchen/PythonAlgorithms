def fruits_into_baskets(fruits):
  maxLen = 0
  k = 2
  winS = 0
  _set = set()

  for winE in range(len(fruits)):
    _set.add(fruits[winE])
    while len(_set) > k:
        _set.discard(fruits[winS])
        winS += 1

    maxLen = max(maxLen, winE - winS + 1)

  return maxLen


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()