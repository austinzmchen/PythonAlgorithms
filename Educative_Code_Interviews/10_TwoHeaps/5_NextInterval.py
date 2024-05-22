from heapq import heappush, heappop


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  # two heaps
  min_start_heap = []
  min_end_heap = []
  for i, inv in enumerate(intervals):
    heappush(min_start_heap, (inv.start, i))
    heappush(min_end_heap, (inv.end, i))

  result = [0] * len(intervals)
  while len(min_end_heap) > 0:
    end, i = heappop(min_end_heap)
    while len(min_start_heap) > 0 and min_start_heap[0][0] < end:
      heappop(min_start_heap)

    if len(min_start_heap) > 0:
      result[i] = min_start_heap[0][1]
    else:
      result[i] = -1

  return result


def main():

  result = find_next_interval(
      [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
      [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()
