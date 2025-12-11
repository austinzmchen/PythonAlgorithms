from collections import deque

def find_order(tasks, prerequisites):
  sorted_order = []
  adj_dict = {}
  in_degrees = {}
  
  for i in range(tasks):
    adj_dict[i] = []
    in_degrees[i] = 0

  for pair in prerequisites:
    start, end = pair[0], pair[1]
    adj_dict.setdefault(start, []).append(end)
    in_degrees[end] += 1

  queue = deque()
  for key, value in in_degrees.items():
    if value == 0:
      queue.append(key)

  while queue:
    size = len(queue)
    for _ in range(size):
      vert = queue.popleft()
      sorted_order.append(vert)

      for adj in adj_dict[vert]:
        in_degrees[adj] -= 1
        if in_degrees[adj] == 0:
          queue.append(adj)

  return sorted_order


def main():
  print("Is scheduling possible: " + 
        str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()