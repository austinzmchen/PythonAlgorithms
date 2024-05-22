
def find_happy_number(num):
  fast, slow = num, num
  while True:
    slow = next_num(slow)
    fast = next_num(next_num(fast))
    if slow == fast:
      return fast == 1
  pass


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