# /*
# Problem Statement #
# There is a dictionary containing words from an alien language for which we don’t know the ordering of the alphabets. 
# Write a method to find the correct order of the alphabets in the alien language. 
# It is given that the input is a valid dictionary and there exists an ordering among its alphabets.

# Example 1:

# Input: Words: ["ba", "bc", "ac", "cab"]
# Output: bac
# Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
# from the given words we can conclude the following ordering among its characters:

# 1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
# 2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

# From the above two points, we can conclude that the correct character order is: "bac"
# Example 2:

# Input: Words: ["cab", "aaa", "aab"]
# Output: cab
# Explanation: From the given words we can conclude the following ordering among its characters:

# 1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
# 2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

# From the above two points, we can conclude that the correct character order is: "cab"
# Example 3:

# Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
# Output: ywxz
# Explanation: From the given words we can conclude the following ordering among its characters:

# 1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
# 2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
# 3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
# 4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
# 5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

# From the above five points, we can conclude that the correct character order is: "ywxz"

# Solution #
# Since the given words are sorted lexicographically by the rules of the alien language, we can always compare two adjacent words to determine the ordering of the characters. Take Example-1 above: [“ba”, “bc”, “ac”, “cab”]

# Take the first two words “ba” and “bc”. Starting from the beginning of the words, find the first character that is different in both words: it would be ‘a’ from “ba” and ‘c’ from “bc”. Because of the sorted order of words (i.e. the dictionary!), we can conclude that ‘a’ comes before ‘c’ in the alien language.
# Similarly, from “bc” and “ac”, we can conclude that ‘b’ comes before ‘a’.
# These two points tell us that we are actually asked to find the topological ordering of the characters, and that the ordering rules should be inferred from adjacent words from the alien dictionary.

# This makes the current problem similar to Tasks Scheduling Order, the only difference being that we need to build the graph of the characters by comparing adjacent words first, and then perform the topological sort for the graph to determine the order of the characters.
#  */

from collections import deque

def find_order(words):
  sorted_order = []
  adj_dict: dict[str, list] = {}
  in_degrees: dict[str, int] = {}

  # we need to build the in_degs and adj_dict of each character and its directions
  # - compare every consecutive pair of word
  # - for every pair of words, compare chars
  for i in range(1, len(words)):
    prev_word = words[i - 1]
    curr_word = words[i]
    
    for j in range(min(len(prev_word), len(curr_word))):
      char1 = prev_word[j]
      char2 = curr_word[j]
      
      if char1 != char2:
        adj_dict.setdefault(char1, []).append(char2)
        
        in_degrees.setdefault(char1, 0)
        in_degrees[char2] = in_degrees.setdefault(char2, 0) + 1
        break

  queue = deque()
  for key, value in in_degrees.items():
    if value == 0:
      queue.append(key)

  while queue:
    size = len(queue)
    for i in range(size):
      vert = queue.popleft()
      sorted_order.append(vert)

      for adj in adj_dict.get(vert, []):
        if adj in in_degrees:
          in_degrees[adj] -= 1
          if in_degrees[adj] == 0:
            queue.append(adj)

  return "".join(sorted_order)


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))
  print("Character order: " + find_order(["zy","zx"]))

main()