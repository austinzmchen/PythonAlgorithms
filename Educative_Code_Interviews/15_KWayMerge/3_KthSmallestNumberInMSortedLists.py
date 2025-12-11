from heapq import heappush, heappop

class DataWrap:
  def __init__(self, value, i_row, i_col) -> None:
    self.value = value
    self.i_row = i_row
    self.i_col = i_col
  
  def __lt__(self, other):
    return self.value < other.value


def find_Kth_smallest(lists, k):
  min_heap = []
  for ls_idx, ls in enumerate(lists):
    # since we don't have linked list, we need to store index to identify the list and node
    heappush(min_heap, DataWrap(ls[0], ls_idx, 0))

  count = 0
  while min_heap:
    wrap = heappop(min_heap)
    
    row = wrap.i_row
    col = wrap.i_col + 1
    # push the next node to the heap
    if col < len(lists[row]):
      heappush(min_heap, DataWrap(lists[row][col], row, col))

    # check k
    count += 1
    if count == k:
      return wrap.value

  pass


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))

main()