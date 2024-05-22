from heapq import *


def find_sum_of_elements(nums, k1, k2):
  maxHeap = []
  for n in nums:
    if len(maxHeap) < k2:
      heappush(maxHeap, DataWrap(n))
    else:
      if n < maxHeap[0].num:
        heappop(maxHeap)        
        heappush(maxHeap, DataWrap(n))

  sum = 0
  while len(maxHeap) > k1:
    pop = heappop(maxHeap)
    if len(maxHeap) + 1 < k2:
      sum += pop.num

  return sum


class DataWrap:
  def __init__(self, num) -> None:
    self.num = num

  def __lt__(self, other):
    return self.num > other.num


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()