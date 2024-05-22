def non_repeat_substring(str):
  maxLen = 0
  currLen = 0

  _set = set()
  for c in str:
    if c in _set:
      currLen = 1
    else:
      currLen += 1
    
    _set.add(c)
    maxLen = max(maxLen, currLen)

  return maxLen


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()