# Problem Statement
# Design a data structure that supports:

# Adding a number from a data stream
# Finding the median of all numbers added so far

# The median is:

# The middle value in an ordered list (odd count)
# The average of the two middle values (even count)
#
# Example
# addNum(1)    → median = 1
# addNum(2)    → median = 1.5 (average of 1 and 2)
# addNum(3)    → median = 2 (middle value)
# addNum(4)    → median = 2.5 (average of 2 and 3)
# addNum(5)    → median = 3 (middle value)
#

from heapq import heappush, heappop

class MedianOfAStream:
  
  # Strategy:
  # - max_heap: stores smaller half (use negative values for max heap)
  # - min_heap: stores larger half
  # - Keep heaps balanced: |max_heap.size - min_heap.size| <= 1
  # - max_heap.size >= min_heap.size (max_heap can have 1 more element)

  min_heap = []
  max_heap = []

  def insert_num(self, num):    
    # Step 1: Balance - ensure max_heap's top <= min_heap's top
    # Move the largest from max_heap to min_heap
    if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
      heappush(self.max_heap, -num)
    else:
      heappush(self.min_heap, num)

    # Step 2: Maintain size property (max_heap.size >= min_heap.size)
    if len(self.max_heap) > len(self.min_heap) + 1:
      heappush(self.min_heap, -heappop(self.max_heap))
    elif len(self.max_heap) < len(self.min_heap):
      heappush(self.max_heap, -heappop(self.min_heap))


  def find_median(self):
    if len(self.max_heap) == len(self.min_heap):
      return (-self.max_heap[0] + self.min_heap[0]) / 2
    else:
      return -self.max_heap[0]


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
