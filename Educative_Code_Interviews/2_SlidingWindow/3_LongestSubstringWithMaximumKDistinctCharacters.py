

def longest_substring_with_k_distinct(str1, k):
  maxLen = 0
  _set = set()
  winStart = 0

  for winEnd in range(len(str1)):
    _set.add(str1[winEnd])
    while len(_set) > k:
        _set.discard(str1[winStart])
        winStart += 1
        
    maxLen = max(maxLen, winEnd - winStart + 1)

  return maxLen

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()