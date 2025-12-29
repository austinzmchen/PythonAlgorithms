# /*
# Problem Statement #
# Given a string, find the length of the longest substring, 
# which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

#  */
 
def non_repeat_substring_1(str):
  res = 0
  curr_len = 0
  _set = set()
  
  for c in str:
    if c in _set:
      curr_len = 1
    else:
      curr_len += 1
    
    _set.add(c)
    res = max(res, curr_len)

  return res


def non_repeat_substring(str):
  res = 0
  win_s = 0
  
  _dict = {} # 0 no delete
  repeated_char_count = 0
  
  for win_e, v in enumerate(str):
    _dict[v] = _dict.setdefault(v, 0) + 1
    if _dict[v] > 1:
      repeated_char_count += 1
      
    while repeated_char_count > 0:
      char_s = str[win_s]
      _dict[char_s] -= 1
      if _dict[char_s] == 1:
        repeated_char_count -= 1
        
      win_s += 1
    
    res = max(res, win_e - win_s + 1)
  return res


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()