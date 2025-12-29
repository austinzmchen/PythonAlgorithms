# 271. Encode and Decode Strings
# Problem Description
# Design an algorithm to encode a list of strings to a single string, and decode that single string back to the original list of strings.
# Implement two functions:

# encode(strs): Encodes a list of strings to a single string
# decode(s): Decodes a single string back to the original list of strings

# Constraints

# The string may contain any possible characters (including delimiter characters)
# The decoded list should be exactly the same as the original list

# # Example 1
# Input: ["Hello", "World"]
# encode() -> some encoded string
# decode(encoded string) -> ["Hello", "World"]

# # Example 2
# Input: [""]
# encode() -> some encoded string
# decode(encoded string) -> [""]

# # Example 3
# Input: []
# encode() -> ""
# decode("") -> []

# # Example 4 (Tricky - strings contain special characters)
# Input: ["a:b", "c#d", "e,f"]
# encode() -> some encoded string
# decode(encoded string) -> ["a:b", "c#d", "e,f"]

# # Example 5 (Edge case - empty strings)
# Input: ["", "a", "", "b"]
# encode() -> some encoded string
# decode(encoded string) -> ["", "a", "", "b"]

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
      res = []

      for str in strs:
        es = f"{len(str)}:{str}"
        res.append(es)

      return "".join(res)


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        i = 0
        res = []

        while i < len(str):
          j = i
          while j < len(str) and str[j] != ':':
            j += 1
            
          size = int(str[i:j])
          i = j + 1
          
          encoded_str = str[i: i + size]
          res.append(encoded_str)
          
          i += size

        return res
      
  
sol = Solution()
print(sol.decode(sol.encode(["Hello", "World"])))
print(sol.decode(sol.encode(["a:b", "c#d", "e,f"])))
print(sol.decode(sol.encode(["", "a", "", "b"])))
