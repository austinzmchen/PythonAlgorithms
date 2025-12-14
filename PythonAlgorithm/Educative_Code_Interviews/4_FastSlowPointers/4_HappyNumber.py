"""
Happy Number (Fast & Slow Pointers Pattern)

Problem:
A happy number is a number where the process of repeatedly replacing the number
by the sum of the squares of its digits eventually leads to 1.

If the process loops endlessly in a cycle that doesn't include 1, the number
is not happy.

Examples:
    Input: 23
    Process: 23 -> 2² + 3² = 4 + 9 = 13
             13 -> 1² + 3² = 1 + 9 = 10
             10 -> 1² + 0² = 1 + 0 = 1
    Output: True (Happy number!)    
"""


def find_happy_number(num) -> bool:
  fast, slow = num, num
  while True:
    slow = next_num(slow)
    fast = next_num(next_num(fast))
    if slow == fast:
      return fast == 1

  return False


def next_num(num) -> int:
  sum = 0
  while num > 0:
    d = num % 10
    sum += d ** 2
    num //= 10
  return sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()