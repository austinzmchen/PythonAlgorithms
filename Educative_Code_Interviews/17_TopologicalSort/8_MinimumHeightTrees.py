from collections import defaultdict, deque


def find_trees(nodes, edges):
  in_degrees = defaultdict(int)
  adj_list = defaultdict(list)
  
  for edge in edges:
    from_node = edge[0]
    to_node = edge[1]
    in_degrees[from_node] += 1
    in_degrees[to_node] += 1
    adj_list[from_node].append(to_node)
    adj_list[to_node].append(from_node)

  q = deque()
  for k, v in in_degrees.items():
    if v == 1:
      q.append(k)

  while len(in_degrees) > 2:
    length = len(q)
    for _ in range(length):
      n = q.popleft()
      del in_degrees[n]

      for adj in adj_list[n]:
        if adj not in in_degrees:
          continue

        in_degrees[adj] -= 1
        if in_degrees[adj] == 1:
          q.append(adj)

  return in_degrees.keys()


def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))


main()
