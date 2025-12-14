from heapq import heappush, heappop

class Interval:
  def __init__(self, list):
    self.start = list[0]
    self.end = list[1]
  
  def __lt__(self, other):
    return self.end < other.end
  
  
class Solution:
    def minMeetingRooms(intervals: List) -> int:
        if (len(intervals) == 0): return 1

        intervals.sort()
        min_heap = []

        # setup
        rooms = 1
        heappush(min_heap, Interval(intervals[0]))

        for i in range(i, len(intervals)):
            inv = intervals[i]
            #  compare the next meeting's start with the end of a current meeting that finishes earliest
            if min_heap and min_heap[0].end > inv[0]:
                rooms += 1
                heappush(min_heap, Interval(inv)) # put this in a new meeting room
            else:
                # put this in a meeting room previsouly used by another meeting but finished
                heappop(min_heap)
                heappush(min_heap, Interval(inv))

        return rooms