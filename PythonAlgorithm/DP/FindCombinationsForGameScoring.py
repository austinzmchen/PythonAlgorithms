from functools import lru_cache


def scoring_options(n):
  @lru_cache
  def recur(num):
    if num < 0:
      return 0
    if num == 0:
      return 1
    i = 1
    count = 0
    while c := recur(num - i):
      count += c
      i *= 2
    return count
  #
  return recur(n)


print(scoring_options(3))
print(scoring_options(5))