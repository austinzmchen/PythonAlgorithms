# /*
# Problem Statement #
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters 
# with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

#  */
 
from typing import DefaultDict


def length_of_longest_substring(str, k):
  res = 0
  win_start = 0
  local_max_repeat = 0
  _dict = DefaultDict(int)

  for win_e, v in enumerate(str):
    _dict[v] += 1
    local_max_repeat = max(local_max_repeat, _dict[v])

    # while k chars not enough to replace the other chars
    while win_e - win_start + 1 - local_max_repeat > k:
      char_s = str[win_start]
      _dict[char_s] -= 1
      win_start += 1
      
      # local_max_repeat not updated, seems that way

    res = max(res, win_e - win_start + 1)

  return res


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()