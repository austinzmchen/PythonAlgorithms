from heapq import *


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')
    
  def __lt__(self, other):
      return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2


class DataWrap:
    def __init__(self, point: Point) -> None:
        self.point = point
    
    def __lt__(self, other):
        return self.point > other.point


def find_closest_points(points, k):
  maxHeap = []
  for i in range(len(points)):
    p = points[i]
    if i < k:
        heappush(maxHeap, DataWrap(p))
    else:
        if p < maxHeap[0].point:
            heappop(maxHeap)
            heappush(maxHeap, DataWrap(p))

  return list([item.point for item in maxHeap])


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()

