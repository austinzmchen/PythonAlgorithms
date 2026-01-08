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

def length_of_longest_substring(str, k):
  res = 0
  repeat_char_count = 0
  _dict = {}
  
  l = 0
  for r, c in enumerate(str):
    _dict[c] = _dict.get(c, 0) + 1
    repeat_char_count = max(repeat_char_count, _dict[c])

    # while k chars not enough to replace the other chars
    while repeat_char_count + k < r - l + 1:
      _dict[str[l]] -= 1
      l += 1
      # We don't need to decrease repeat_char_count when shrinking because we only care about finding a window that's LONGER than our current best.

    res = max(res, r - l + 1)
  return res


def length_of_longest_substring(s, k):
    res = 0

    _dict = {}
    l = 0
    curr_max = 0 # max repeating chars count

    for r, c in enumerate(s):
        _dict[c] = _dict.get(c, 0) + 1
        # update curr max
        curr_max = max(curr_max, _dict[c])

        while curr_max + k < r - l + 1:
            _dict[s[l]] -= 1
            
            l += 1
            # update curr max
            curr_max = max(_dict.values())

        res = max(res, r - l + 1)

    return res


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))

main()