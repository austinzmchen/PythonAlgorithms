from heapq import heappush, heappop

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  # two heaps
  min_heap_start = []
  min_heap_end = []
  
  for i, inv in enumerate(intervals):
    heappush(min_heap_start, (inv.start, i))
    heappush(min_heap_end, (inv.end, i))

  result = [0] * len(intervals)
  
  # pop min_heap_end from lowest to get the next inv
  while min_heap_end:
    end, i = heappop(min_heap_end)
    # for this inv, find the next inv whose start >= end
    
    while min_heap_start and min_heap_start[0][0] < end:
      heappop(min_heap_start)

    if min_heap_start:
      result[i] = min_heap_start[0][1]
    else:
      result[i] = -1
  #
  return result


def main():
  result = find_next_interval(
      [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
      [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))

main()
