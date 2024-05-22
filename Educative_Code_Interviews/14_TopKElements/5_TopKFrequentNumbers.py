from typing import DefaultDict
from heapq import *

def find_k_frequent_numbers(nums, k):
  _ddict = DefaultDict(int)
  for n in nums:
    _ddict[n] += 1

  minHeap = []
  for num, freq in _ddict.items():
    if len(minHeap) < k:
      heappush(minHeap, num)
    else:
      if freq > _ddict[minHeap[0]]:
        heappop(minHeap)
        heappush(minHeap, num)

  return minHeap


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
