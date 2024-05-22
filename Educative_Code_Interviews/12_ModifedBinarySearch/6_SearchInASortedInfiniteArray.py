import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):
  size = 1
  end_idx = size - 1
  while reader.get(end_idx) != math.inf:
    size *= 2
    end_idx = size - 1
  
  l, r = 0, end_idx
  while l <= r:
    mid = l + (r - l) // 2
    if reader.get(mid) == key:
      return mid
    
    if key < reader.get(mid):
      r = mid - 1
    else:
      l = mid + 1
      
  return -1


def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()
