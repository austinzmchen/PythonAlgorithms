from heapq import *


def find_closest_elements(arr, K, X):
  class DataWrap:
    def __init__(self, num) -> None:
      self.num = num

    def __lt__(self, other):
      return abs(self.num - X) > abs(other.num - X)

  maxHeap = []
  for n in arr:
    if len(maxHeap) < K:
      heappush(maxHeap, DataWrap(n))
    else:
      if abs(n - X) < abs(maxHeap[0].num - X):
        heappop(maxHeap)
        heappush(maxHeap, DataWrap(n))

  return sorted([v.num for v in maxHeap])


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()