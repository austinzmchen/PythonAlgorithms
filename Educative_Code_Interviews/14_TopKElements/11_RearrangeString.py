# Problem Statement #
# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

# Example 1:
# Input: "aappp"
# Output: "papap"
# Explanation: In "papap", none of the repeating characters come next to each other.

# Example 2:
# Input: "Programming"
# Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
# Explanation: None of the repeating characters come next to each other.

# Example 3:
# Input: "aapa"
# Output: ""
# Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".

# Solution #
# This problem follows the Top ‘K’ Numbers pattern. We can follow a greedy approach to find an arrangement of the given string where no two same characters come next to each other.
# We can work in a stepwise fashion to create a string with all characters from the input string. Following a greedy approach, we should first append the most frequent characters to the output strings, for which we can use a Max Heap. By appending the most frequent character first, we have the best chance to find a string where no two same characters come next to each other.
# So in each step, we should append one occurrence of the highest frequency character to the output string. We will not put this character back in the heap to ensure that no two same characters are adjacent to each other. In the next step, we should process the next most frequent character from the heap in the same way and then, at the end of this step, insert the character from the previous step back to the heap after decrementing its frequency.
# Following this algorithm, if we can append all the characters from the input string to the output string, we would have successfully found an arrangement of the given string where no two same characters appeared adjacent to each other.

from heapq import heappop, heappush

def rearrange_string(str):
  freq_dict = {}
  for c in str:
    freq_dict[c] = freq_dict.setdefault(c, 0) + 1

  max_heap = []
  for c, freq in freq_dict.items():
    heappush(max_heap, (-freq, c))

  res = []
  while max_heap:
    freq, c = heappop(max_heap)
    
    if res and res[-1] == c:
      return ""

    res.append(c)
    if -freq > 1:
      heappush(max_heap, (-(-freq-1), c)) # decrement 1 then add back to heap as negative number

  return "".join(res)


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))

main()