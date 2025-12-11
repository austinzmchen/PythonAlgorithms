"""
Kth Smallest Number in a Sorted Matrix

Problem: Given an n x n matrix where each row and column is sorted in ascending order,
find the kth smallest element in the matrix.

Example:
    Input: matrix = [[1,5,9],
                     [10,11,13],
                     [12,13,15]], k = 8
    Output: 13
    
Note: It's the 8th smallest element, not the 8th distinct element.
"""

from heapq import heappush, heappop

class DataWrap:
  def __init__(self, value, i_row, i_col) -> None:
    self.value = value
    self.i_row = i_row
    self.i_col = i_col

  def __lt__(self, other):
    return self.value < other.value


# solution is same as previous
#   - This binary search optimization only works for the matrix, not for independent lists,
#     because the lists have no relationship to each other.
def find_Kth_smallest(matrix, k):
  min_heap = []
  for i, ls in enumerate(matrix):
    heappush(min_heap, DataWrap(ls[0], i, 0))

  count = 0
  while min_heap:
    wrap = heappop(min_heap)
    
    row = wrap.i_row
    col = wrap.i_col + 1
    
    if col < len(matrix[row]):
      heappush(min_heap, DataWrap(matrix[row][col], row, col))

    count += 1
    if count == k:
      return wrap.value

  pass


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

main()