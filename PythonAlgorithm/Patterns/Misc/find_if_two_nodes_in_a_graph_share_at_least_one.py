#  Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.
#
#  For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.
#
#               15
#               |
#           14  13
#           |   |
#  1   2    4   12
#   \ /   / | \ /
#    3   5  8  9
#     \ / \     \
#      6   7     11
#
parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9),(15, 13)
]
#  Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.
#
#  Sample input and output:
#
#  hasCommonAncestor(parentChildPairs1, 3, 8) => false
#  hasCommonAncestor(parentChildPairs1, 5, 8) => true
#  hasCommonAncestor(parentChildPairs1, 6, 8) => true
#  hasCommonAncestor(parentChildPairs1, 6, 9) => true
#  hasCommonAncestor(parentChildPairs1, 1, 3) => false
#  hasCommonAncestor(parentChildPairs1, 3, 1) => false
#  hasCommonAncestor(parentChildPairs1, 7, 11) => true
#  hasCommonAncestor(parentChildPairs1, 6, 5) => true
#  hasCommonAncestor(parentChildPairs1, 5, 6) => true
#  Additional example: In this diagram, 4 and 12 have a common ancestor of 11.
#
#          11
#         /  \
#        10   12
#       /  \
#  1   2    5
#   \ /    / \
#    3    6   7
#     \        \
#      4        8
#
parentChildPairs2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2),
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8),
]
#
#  hasCommonAncestor(parentChildPairs2, 4, 12) => true
#  hasCommonAncestor(parentChildPairs2, 1, 6) => false
#  hasCommonAncestor(parentChildPairs2, 1, 12) => false
#
#  n: number of pairs in the input


from collections import defaultdict

# iterative
def find_common1(pairs, node1, node2):
  _dict = defaultdict(set)
  for p in pairs:
    _dict[p[1]].add(p[0])
  #
  list1 = [node1] if len(_dict[node1]) > 0 else []
  i1 = 0
  while i1 < len(list1):
    for parent in _dict[list1[i1]]:
      list1.append(parent)
    i1 += 1
  # 
  list2 = [node2]
  i2 = 0
  set1 = set(list1)
  while i2 < len(list2):
    for parent in _dict[list2[i2]]:
      if parent in set1:
        return True
      if parent not in list2:
        list2.append(parent)
    i2 += 1
  #
  return False


# recursive
def find_common(pairs, node1, node2):
  _dict = defaultdict(set)
  for p in pairs:
    _dict[p[1]].add(p[0])
  #
  def dfs(root, dict, visited):
    for parent in dict[root]:
      visited.add(parent)
      dfs(parent, dict, visited)
  #
  set1 = set()
  dfs(node1, _dict, set1)
  #
  def dfs2(root, dict, visited) -> bool:
    for parent in dict[root]:
      if parent in visited or \
        dfs2(parent, dict, visited):
        return True
    return False
  # 
  return dfs2(node2, _dict, set1)


print(find_common(parentChildPairs2, 4, 12))
print(find_common(parentChildPairs2, 1, 6))
print(find_common(parentChildPairs2, 1, 12))
print()
print(find_common(parentChildPairs1, 3, 8))
print(find_common(parentChildPairs1, 5, 8))
print(find_common(parentChildPairs1, 6, 8))
print(find_common(parentChildPairs1, 6, 9))
print(find_common(parentChildPairs1, 1, 3))
print(find_common(parentChildPairs1, 3, 1))
print(find_common(parentChildPairs1, 7, 11))
print(find_common(parentChildPairs1, 6, 5))
print(find_common(parentChildPairs1, 5, 6))