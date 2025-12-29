from collections import deque

def is_scheduling_possible(tasks, prerequisites):
  sorted_order = []
  adj_dict = {}
  in_degrees = {}
  
  for i in range(tasks):
    in_degrees[i] = 0
    adj_dict[i] = []

  for pair in prerequisites:
    start, end = pair[0], pair[1]
    adj_dict.setdefault(start, []).append(end)
    in_degrees[end] += 1

  queue = deque()
  for key, value in in_degrees.items():
    # if the who list is a circle, nothing will be added to queue
    if value == 0:
      queue.append(key)

  while queue:
    size = len(queue)
    for i in range(size):
      vert = queue.popleft()
      sorted_order.append(vert)

      for adj in adj_dict[vert]:
        in_degrees[adj] -= 1
        # if there are circles, the circle starting vert wont have in_degs == 0
        if in_degrees[adj] == 0:
          queue.append(adj)

  return len(sorted_order) == tasks


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()