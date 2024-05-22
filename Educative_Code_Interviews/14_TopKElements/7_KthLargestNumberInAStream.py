from heapq import *


class KthLargestNumberInStream:
  def __init__(self, nums, k):
    self._minHeap = []
    self.k = k
    for n in nums:
      self.add(n)


  def add(self, num):
    if len(self._minHeap) < self.k:
      heappush(self._minHeap, num)        
    else:
      if num > self._minHeap[0]:
        heappop(self._minHeap)
        heappush(self._minHeap, num)        

    return self._minHeap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
