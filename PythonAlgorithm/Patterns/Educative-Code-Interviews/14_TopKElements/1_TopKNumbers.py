
from heapq import heappop, heappush

def find_k_largest_numbers(nums, k):
  min_heap = []
  
  for i, num in enumerate(nums):
    if i < k:
      heappush(min_heap, num)
    else:
      if num > min_heap[0]:
        heappop(min_heap)
        heappush(min_heap, num)

  # the heap has the top 'K' numbers, return them in a list
  return list(min_heap)


def main():
  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))

main()