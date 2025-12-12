from heapq import heappop, heappush

def find_sum_of_elements(nums, k1, k2):
  max_heap = []
  for n in nums:
    if len(max_heap) < k2:
      heappush(max_heap, -n)
    else:
      if n < -max_heap[0]:
        heappop(max_heap)        
        heappush(max_heap, -n)

  heappop(max_heap) # pop 1 to exclude the k2-th number
  sum = 0
  
  while len(max_heap) > k1:
    pop = heappop(max_heap)
    sum += -pop

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