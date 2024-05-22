from heapq import *

def find_k_largest_numbers(nums, k):
  minHeap = []
  for i in range(len(nums)):
    if i < k:
      heappush(minHeap, nums[i])
    else:
      if nums[i] > minHeap[0]:
        heappop(minHeap)
        heappush(minHeap, nums[i])

  # the heap has the top 'K' numbers, return them in a list
  return list(minHeap)


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()