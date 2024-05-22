import sys
from heapq import heappush, heappop


class DataWrap:
  def __init__(self, value, row_idx, col_idx) -> None:
    self.value = value
    self.row_idx = row_idx
    self.col_idx = col_idx
  
  def __lt__(self, other):
    return self.value < other.value


def find_Kth_smallest(lists, k):
  min_heap = []
  for i in range(len(lists)):
    heappush(min_heap, DataWrap(lists[i][0], i, 0))

  count = 0
  while len(min_heap) > 0:
    data = heappop(min_heap)
    if data.col_idx + 1 < len(lists[data.row_idx]):
      ci = data.col_idx + 1
      heappush(min_heap, DataWrap(
          lists[data.row_idx][ci], data.row_idx, ci))

    count += 1
    if count == k:
      return data.value

  pass


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
