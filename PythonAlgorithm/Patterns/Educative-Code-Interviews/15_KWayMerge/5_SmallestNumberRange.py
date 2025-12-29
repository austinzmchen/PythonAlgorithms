"""
Smallest Number Range

Problem: Given K sorted lists, find the smallest range that includes 
at least one number from each of the K lists.

Example:
    Input: [[1, 5, 8], [4, 12], [7, 8, 10]]
    Output: [4, 7]
    Explanation: Range [4,7] contains 5 from list 1, 4 from list 2, 7 from list 3
    
Key Insight: 
- We need one element from EACH list
- Range = [min_element, max_element] among selected elements
- To minimize range, we want to increase min while keeping max small
"""

from heapq import heappush, heappop

class DataWrap:
  
  def __init__(self, value, i_row, i_col) -> None:
    self.value = value
    self.i_row = i_row
    self.i_col = i_col

  def __lt__(self, other):
    return self.value < other.value


def find_smallest_range_1(lists):
  import sys
  num_large = -sys.maxsize - 1
  num_small = 0
  diff = sys.maxsize

  min_heap = []
  for i, ls in enumerate(lists):
    heappush(min_heap, DataWrap(ls[0], i, 0))
    num_large = max(num_large, ls[0])

  while min_heap:
    wrap = heappop(min_heap)
    
    if num_large - wrap.value < diff:
      num_small = wrap.value
      diff = num_large - wrap.value

    row = wrap.i_row
    col = wrap.i_col + 1
    
    if col < len(lists[row]):
      heappush(min_heap, DataWrap(lists[row][col], row, col))
      num_large = max(num_large, lists[row][col])
      
    else:
      break

  return [num_small, num_small + diff]


def find_smallest_range(lists):
  range_start, range_end = 0, float('inf')
  curr_max = float('-inf')

  min_heap = []
  for i, ls in enumerate(lists):
    heappush(min_heap, (ls[0], i, 0))
    curr_max = max(curr_max, ls[0])

  while min_heap:
    curr_min, row, col = heappop(min_heap)
    
    if curr_max - curr_min < range_end - range_start:
      range_start, range_end = curr_min, curr_max

    if col + 1 < len(lists[row]):
      next_val = lists[row][col+1]
      heappush(min_heap, (next_val, row, col+1))
      curr_max = max(curr_max, next_val)
      
    else:
      # This list is exhausted, we're done
      break

  return [range_start, range_end]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))

main()