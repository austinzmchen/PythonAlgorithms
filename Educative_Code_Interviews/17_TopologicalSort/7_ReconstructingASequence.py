from collections import defaultdict, deque


def can_construct(originalSeq, sequences):
  in_degrees = defaultdict(int)
  adj_list = defaultdict(list)
  for seq in sequences:
    for i in range(len(seq) - 1):
      from_node = seq[i]
      to_node = seq[i + 1]
      if from_node not in in_degrees:
        in_degrees[from_node] = 0
      in_degrees[to_node] += 1
      adj_list[from_node].append(to_node)

  q = deque()
  for k, v in in_degrees.items():
    if v == 0:
      q.append(k)

  i = 0
  while len(q) > 0:
    if len(q) > 1 or q[0] != originalSeq[i]:
      return False
    
    n = q.popleft()
    for adj in adj_list[n]:
      in_degrees[adj] -= 1
      if in_degrees[adj] == 0:
        q.append(adj)

    i += 1

  return True


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
