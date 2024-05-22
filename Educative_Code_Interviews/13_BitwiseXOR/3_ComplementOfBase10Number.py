def calculate_bitwise_complement(n):
  m = n
  count = 0
  while m != 0:
    m = m >> 1
    count += 1
  
  all_ones = (1 << count) - 1
  return all_ones ^ n


def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
