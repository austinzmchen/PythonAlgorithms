from heapq import heappush, heappop
import sys


class DataWrap:
  def __init__(self, value, row_idx, col_idx) -> None:
    self.value = value
    self.row_idx = row_idx
    self.col_idx = col_idx

  def __lt__(self, other):
    return self.value < other.value


def find_smallest_range(lists):
  num_large = -sys.maxsize - 1
  num_small = 0
  diff = sys.maxsize

  min_heap = []
  for i in range(len(lists)):
    heappush(min_heap, DataWrap(lists[i][0], i, 0))
    num_large = max(num_large, lists[i][0])


  while len(min_heap) > 0:
    data = heappop(min_heap)
    if num_large - data.value < diff:
      num_small = data.value
      diff = num_large - data.value

    if data.col_idx + 1 < len(lists[data.row_idx]):
      ci = data.col_idx + 1
      heappush(min_heap, DataWrap(
          lists[data.row_idx][ci], data.row_idx, ci))

      num_large = max(num_large, lists[data.row_idx][ci])
    else:
      break

  return [num_small, num_small + diff]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
