from heapq import *

class job:
  
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load
  
  def __lt__(self, other):
    return self.end < other.end


def find_max_cpu_load(jobs):
  min_heap = []
  jobs.sort(key=lambda x: x.start)
  import sys
  max_load = -sys.maxsize - 1
  curr_load = 0

  for _, job in enumerate(jobs):
    while len(min_heap) > 0 and min_heap[0].end <= job.start:
      jb = heappop(min_heap)
      curr_load -= jb.cpu_load
      
    curr_load += job.cpu_load
    heappush(min_heap, job)
    max_load = max(max_load, curr_load)

  return max_load


def main():
  print("Maximum CPU load at any time: " +
        str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " +
        str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " +
        str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
