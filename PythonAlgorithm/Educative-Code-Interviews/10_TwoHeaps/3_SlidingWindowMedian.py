from heapq import heappop, heappush, heapify


class SlidingWindowMedian:

  def __init__(self) -> None:
    self.min_heap = []
    self.max_heap = []


  def add(self, num):
    if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
      heappush(self.max_heap, -num)
    else:
      heappush(self.min_heap, num)
    self.rebalance()


  def find_median(self) -> float:
    if len(self.max_heap) == len(self.min_heap):
      return (-self.max_heap[0] + self.min_heap[0]) / 2 
    else:
      return -self.max_heap[0]


  def remove(self, num):
    # remove from heap is not O(1), need heapify re-heap
    if num <= -self.max_heap[0]:
      self.max_heap.remove(-num)
      heapify(self.max_heap)
    else:
      self.min_heap.remove(num)
      heapify(self.min_heap)
    self.rebalance()


  def rebalance(self):
    if len(self.max_heap) > len(self.min_heap) + 1:
      heappush(self.min_heap, -heappop(self.max_heap))
    elif len(self.max_heap) < len(self.min_heap):
      heappush(self.max_heap, -heappop(self.min_heap))


  def find_sliding_window_median(self, nums, k):
    res = []
    for i in range(len(nums)):
      self.add(nums[i])
      if i >= k:
        self.remove(nums[i - k])
      if i >= k - 1:
        res.append(self.find_median())
      
    return res


def main():
  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
      [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
      [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()
