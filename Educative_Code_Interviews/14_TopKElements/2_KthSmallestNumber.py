from heapq import *


def find_Kth_smallest_number(nums, k):
    maxHeap = []

    for i in range(len(nums)):
        if i < k:
            heappush(maxHeap, -nums[i])
        else:
            if -nums[i] > maxHeap[0]:
                heappop(maxHeap)
                heappush(maxHeap, -nums[i])
    
    return -maxHeap[0]


def find_Kth_smallest_number2(nums, k):
    class DataWrap:
        def __init__(self, data) -> None:
            self.data = data
        
        def __lt__(self, other):
            return self.data > other.data

    maxHeap = []
    for i in range(len(nums)):
        if i < k:
            heappush(maxHeap, DataWrap(nums[i]))
        else:
            if nums[i] < maxHeap[0].data:
                heappop(maxHeap)
                heappush(maxHeap, DataWrap(nums[i]))
    
    return maxHeap[0].data


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number2([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number2([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number2([5, 12, 11, -1, 12], 3)))


main()
