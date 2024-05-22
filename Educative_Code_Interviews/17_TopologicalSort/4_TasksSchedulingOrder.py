from collections import deque


def find_order(tasks, prerequisites):
  sortedOrder = []
  adj_dict = {}
  in_degrees = {}
  for i in range(tasks):
    adj_dict[i] = []
    in_degrees[i] = 0

  for pair in prerequisites:
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
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
