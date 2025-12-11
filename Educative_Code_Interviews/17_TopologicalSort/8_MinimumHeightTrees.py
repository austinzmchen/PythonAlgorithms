# Problem Overview:
# Given an undirected tree with n nodes, find all nodes that, when chosen as the root, produce a tree with minimum height.
#
# Key Insight:
# The roots of minimum height trees are the center nodes of the graph. There can be at most 2 centers in any tree!

from collections import deque

def find_trees_1(nodes, edges):
  adj_dict: dict[str, list] = {}
  in_degrees: dict[str, int] = {}
  
  # un-directed tree, so every edge counts as 1
  for edge in edges:
    node1 = edge[0]
    node2 = edge[1]
    
    in_degrees[node1] = in_degrees.setdefault(node1, 0) + 1
    in_degrees[node2] = in_degrees.setdefault(node2, 0) + 1
    adj_dict.setdefault(node1, []).append(node2)
    adj_dict.setdefault(node2, []).append(node1)

  queue = deque()
  for k, v in in_degrees.items():
    if v == 1:
      # these are the leave node/vert
      queue.append(k)

  while len(in_degrees) > 2:
    size = len(queue)
    for _ in range(size):
      vert = queue.popleft()
      del in_degrees[vert]

      for adj in adj_dict.get(vert, []):
        if adj in in_degrees:
          in_degrees[adj] -= 1
          if in_degrees[adj] == 1:
            queue.append(adj)

  return in_degrees.keys()


def find_trees(nodes, edges):
  adj_dict: dict[str, list] = {}
  in_degrees: dict[str, int] = {}
  
  # un-directed tree, so every edge counts as 1
  for edge in edges:
    node1 = edge[0]
    node2 = edge[1]
    
    in_degrees[node1] = in_degrees.setdefault(node1, 0) + 1
    in_degrees[node2] = in_degrees.setdefault(node2, 0) + 1
    adj_dict.setdefault(node1, []).append(node2)
    adj_dict.setdefault(node2, []).append(node1)

  queue = deque()
  for k, v in in_degrees.items():
    if v == 1:
      # these are the leave node/vert
      queue.append(k)

  copy = [] # copy the last round of nodes remaining in the queue
  while queue:
    size = len(queue)
    copy = list(queue)
    
    for _ in range(size):
      vert = queue.popleft()
      in_degrees[vert] -= 1

      for adj in adj_dict.get(vert, []):
        if adj in in_degrees:
          in_degrees[adj] -= 1
          if in_degrees[adj] == 1:
            queue.append(adj)

  return copy


def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))

main()