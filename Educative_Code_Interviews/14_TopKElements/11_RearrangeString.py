from heapq import *
from typing import DefaultDict


def rearrange_string(str):
  _ddict = DefaultDict(int)
  for c in str:
    _ddict[c] += 1

  maxHeap = []
  for c, freq in _ddict.items():
    heappush(maxHeap, DataWrap(c, freq))

  result = []
  while len(maxHeap) > 0:
    pop = heappop(maxHeap)
    if len(result) > 0 and result[-1] == pop.char:
      return ""

    result.append(pop.char)
    if pop.freq > 1:
      heappush(maxHeap, DataWrap(pop.char, pop.freq - 1))

  return "".join(result)


class DataWrap:
  def __init__(self, char: str, freq: int) -> None:
      self.char = char
      self.freq = freq

  def __lt__(self, other):
    return self.freq > other.freq


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()
