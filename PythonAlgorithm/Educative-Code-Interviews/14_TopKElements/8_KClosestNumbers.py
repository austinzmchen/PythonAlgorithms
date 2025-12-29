
from heapq import heappop, heappush

def find_closest_elements(arr, K, X):
  max_heap = []
  
  for i, n in enumerate(arr):
    if i < K:
      heappush(max_heap, (-abs(n-X), n))
    else:
      if abs(n - X) < -max_heap[0][0]:
        heappop(max_heap)
        heappush(max_heap, (-abs(n-X), n))

  return sorted([t[1] for t in max_heap])


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))

main()