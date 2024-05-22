from heapq import *
from typing import DefaultDict, Tuple


def sort_character_by_frequency(str):
  _ddict = DefaultDict(int)
  for c in str:
    _ddict[c] += 1

  maxHeap = []
  for c, freq in _ddict.items():
    heappush(maxHeap, DataWrap((c, freq)))
    
  result = []
  while len(maxHeap) > 0:
    c, freq = heappop(maxHeap).info
    result.append(c * freq)

  return "".join(result)


class DataWrap:
  def __init__(self, info: Tuple) -> None:
    self.info = info

  def __lt__(self, other):
    return self.info[1] > other.info[1]


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()