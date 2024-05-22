from heapq import heappush, heappop
import sys


class DataWrap:
  def __init__(self, value, row_idx, col_idx) -> None:
    self.value = value
    self.row_idx = row_idx
    self.col_idx = col_idx

  def __lt__(self, other):
    return self.value < other.value


def find_Kth_smallest(matrix, k):
  min_heap = []
  for i in range(len(matrix)):
    heappush(min_heap, DataWrap(matrix[i][0], i, 0))

  count = 0
  while len(min_heap) > 0:
    data = heappop(min_heap)
    if data.col_idx + 1 < len(matrix[data.row_idx]):
      ci = data.col_idx + 1
      heappush(min_heap, DataWrap(
          matrix[data.row_idx][ci], data.row_idx, ci))

    count += 1
    if count == k:
      return data.value

  pass


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
