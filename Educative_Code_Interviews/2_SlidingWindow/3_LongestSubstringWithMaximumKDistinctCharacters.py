# /*
# Problem Statement #
# Given a string, find the length of the longest substring in it 
# with no more than K distinct characters.
#
# You can assume that K is less than or equal to the length of the given string.
#
# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

# Time Complexity #
# The above algorithm’s time complexity will be O(N), where N is the number of characters in the input string.
# The outer for loop runs for all characters, and the inner while loop processes each character only once;
# therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).

#  */

def longest_substring_with_k_distinct(str1, k):
  max_len = 0
  _dict: dict[str, int] = {} # tracks char count
  win_s = 0

  for win_e, v in enumerate(str1):
    _dict[v] = _dict.setdefault(v, 0) + 1
    
    while len(_dict) > k:
      s_char = str1[win_s]
      _dict[s_char] -= 1
      if _dict[s_char] == 0:
        del _dict[s_char]
          
      win_s += 1
        
    max_len = max(max_len, win_e - win_s + 1)
  return max_len


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()