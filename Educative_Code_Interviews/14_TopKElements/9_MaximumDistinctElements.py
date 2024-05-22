from heapq import *
from typing import DefaultDict


def find_maximum_distinct_elements(nums, k):
  _ddict = DefaultDict(int)
  for n in nums:
    _ddict[n] += 1

  distincts = 0
  minHeap = []

  for n, freq in _ddict.items():
    if freq == 1:
      distincts += 1
    else:
      heappush(minHeap, (freq, n))

  while len(minHeap) > 0 and k > 0:
    pop = heappop(minHeap)
    if k >= pop[0] - 1:
      distincts += 1
    k -= pop[0] - 1

  return distincts - k if k > 0 else distincts


def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
