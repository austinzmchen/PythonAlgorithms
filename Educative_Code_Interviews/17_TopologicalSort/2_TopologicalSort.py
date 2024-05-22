from collections import deque

def topological_sort(vertices, edges):
  sortedOrder = []
  adj_dict = {}
  in_degrees = {}
  for i in range(vertices):
    adj_dict[i] = []
    in_degrees[i] = 0

  for pair in edges:
    adj_dict[pair[0]].append(pair[1])
    in_degrees[pair[1]] += 1

  queue = deque()
  for key, value in in_degrees.items():
    if value == 0:
      queue.append(key)

  while len(queue) > 0:
    size = len(queue)
    for i in range(size):
      n = queue.popleft()
      sortedOrder.append(n)

      for adj in adj_dict[n]:
        in_degrees[adj] -= 1
        if in_degrees[adj] == 0:
          queue.append(adj)

  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
