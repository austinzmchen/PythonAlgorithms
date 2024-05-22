from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
  sum = 0
  
  minHeap = []
  for l in ropeLengths:
    heappush(minHeap, l)

  while len(minHeap) > 1:
    a = heappop(minHeap)
    b = heappop(minHeap)
    sum += a + b
    heappush(minHeap, a + b)

  return sum


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
