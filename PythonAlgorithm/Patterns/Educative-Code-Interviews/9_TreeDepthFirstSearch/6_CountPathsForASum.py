# Problem Statement
# Given a binary tree and a target sum S, count all paths where the sum of node values equals S.
# 
# Important:
#   - A path can start and end at any node (doesn't have to be root to leaf)
#   - The path must go downward (parent to child direction only)

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths_1(root, S):
  path = []
  
  def recur(node, sum, count) -> int:
    if not node:
      return 0
    
    path.append(node.val)

    curr_count = count
    curr_sum = 0
    for i in range(len(path) - 1, -1, -1):
      curr_sum += path[i]
      if curr_sum == sum:
        curr_count += 1

    curr_count += recur(node.left, sum, curr_count) + \
                  recur(node.right, sum, curr_count)

    del path[-1]
    return curr_count
  #
  return recur(root, S, 0)


def count_paths(root, S):
  path = []
  res = 0
  
  def recur(node, sum):
    if not node:
      return
    path.append(node.val)

    nonlocal res
    curr_sum = 0
    for _, v in enumerate(path[::-1]):
      curr_sum += v
      if curr_sum == sum:
        res += 1

    recur(node.left, sum)
    recur(node.right, sum)

    del path[-1]
  #
  recur(root, S)
  return res


def main():
  # Tree Structure:
  #        12
  #       /   \
  #      7     1
  #    /      /  \
  #   4      10   5
  
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))
  # 2 paths because 7 - 4, 1 - 10

main()
