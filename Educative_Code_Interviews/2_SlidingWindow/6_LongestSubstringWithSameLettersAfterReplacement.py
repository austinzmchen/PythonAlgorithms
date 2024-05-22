from typing import DefaultDict


def length_of_longest_substring(str, k):
  maxLen = 0
  winS = 0
  currMax = 0
  _dict = DefaultDict(int)

  for winE in range(len(str)):
    _dict[str[winE]] += 1
    currMax = max(currMax, _dict[str[winE]])

    while winE - winS + 1 - currMax > k:
        _dict[str[winS]] -= 1
        winS += 1

    maxLen = max(maxLen, winE - winS + 1)

  return maxLen


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()