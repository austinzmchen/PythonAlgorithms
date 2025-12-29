# /*
# Problem Statement #
# Given a string, find all of its permutations preserving the character sequence but changing case.
#
# Example 1:
# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"

# Example 2:
# Input: "ab7c"
# Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

# Solution #
# This problem follows the Subsets pattern and can be mapped to Permutations.
# Let’s take Example-2 mentioned above to generate all the permutations. Following a BFS approach, we will consider one character at a time. 
# Since we need to preserve the character sequence, we can start with the actual string and process each character (i.e., make it upper-case or lower-case) one by one:

# Starting with the actual string: "ab7c"
# Processing the first character (‘a’), we will get two permutations: "ab7c", "Ab7c"
# Processing the second character (‘b’), we will get four permutations: "ab7c", "Ab7c", "aB7c", "AB7c"
# Since the third character is a digit, we can skip it.
# Processing the fourth character (‘c’), we will get a total of eight permutations: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
# Let’s analyze the permutations in the 3rd and the 5th step. How can we generate the permutations in the 5th step from the permutations in the 3rd step?

# If we look closely, we will realize that in the 5th step, when we processed the new character (‘c’), 
# we took all the permutations of the previous step (3rd) and changed the case of the letter (‘c’) in them to create four new permutations.
#  */
 
 
def find_letter_case_string_permutations(str) -> list:
  perms = []
  perms.append("")

  for c in str:
    size = len(perms)
    for i in range(size):
      p = perms[0]
      del perms[0]

      if c.isalpha():
        perms.append(f"{p}{c.lower()}")
        perms.append(f"{p}{c.upper()}")
      else:
        perms.append(f"{p}{c}")

  return perms


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))

main()
