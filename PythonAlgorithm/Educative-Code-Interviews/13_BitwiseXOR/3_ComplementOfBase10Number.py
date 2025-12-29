# Problem Statement
# Given a positive integer, return its complement. The complement is the number you get by flipping all bits in its binary representation (0s become 1s, 1s become 0s).
# Examples:

# Input: 5 (binary: 101) → Output: 2 (binary: 010)
# Input: 7 (binary: 111) → Output: 0 (binary: 000)
# Input: 10 (binary: 1010) → Output: 5 (binary: 0101)

# The key insight: Create a mask of all 1s with the same length as the number, then XOR.
def calculate_bitwise_complement(num):
  # find the bit length
  # in python, it could be `count = num.bit_length()`
  m = num
  count = 0
  while m != 0:
    m = m >> 1
    count += 1
  
  # Create a mask with all 1s of the same length
  # For example: if num = 5 (101), mask = 111 (7)
  all_ones = (1 << count) - 1
  
  # XOR num with mask to flip all bits
  return all_ones ^ num


def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()
