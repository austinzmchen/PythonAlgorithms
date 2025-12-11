# Problem Statement
# Given a non-empty array of integers where every element appears twice except for one, find that single element that appears only once.
# Example:

# Input: [2,2,1] → Output: 1
# Input: [4,1,2,1,2] → Output: 4
#
# The key insight is using the XOR bitwise operation:
#
# a ^ a = 0 (any number XOR itself equals 0)
# a ^ 0 = a (any number XOR 0 equals itself)
# XOR is commutative and associative

def find_single_number(arr):
  num = 0
  for _, v in enumerate(arr):
    num ^= v
  return num


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main()
