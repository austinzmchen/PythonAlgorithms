from collections import deque

def topological_sort(vertices, edges):
  sorted_order = []
  adj_dict = {}
  in_degrees = {}
  
  # need to build in_degree and adj_dict
  for i in range(vertices):
    in_degrees[i] = 0
    adj_dict[i] = []

  for pair in edges:
    start, end = pair[0], pair[1]
    adj_dict.setdefault(start, []).append(end)
    in_degrees[end] += 1

  queue = deque()
  # first the root vert to the queue
  for vert, degs in in_degrees.items():
    if degs == 0:
      queue.append(vert)

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
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()