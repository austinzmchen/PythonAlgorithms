from heapq import heappop, heappush

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')
    
  def __lt__(self, other):
      return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2
    

def find_closest_points(points, k):
  max_heap: list[tuple] = []
    
  def point_val(point: Point) -> float:
    return point.x ** 2 + point.y ** 2

  for i, p in enumerate(points):
    if i < k:
        heappush(max_heap, (-point_val(p), p))
    else:
        if point_val(p) < -max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (-point_val(p), p))

  return [t[1] for t in max_heap]


def main():
  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()

main()