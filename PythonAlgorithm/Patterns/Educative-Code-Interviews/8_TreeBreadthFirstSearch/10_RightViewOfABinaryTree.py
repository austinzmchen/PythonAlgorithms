from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  res = []
  deq = deque()
  deq.append(root)

  while deq:
    length = len(deq)
    for i in range(length):
      n = deq.popleft()
      
      if i == length - 1:
        res.append(n)

      if n.left:
        deq.append(n.left)
      if n.right:
        deq.append(n.right)
  #
  return res


def main():
  # Tree Structure:
  #        12
  #       /   \
  #      7     1
  #    /      /  \
  #   9      10   5
  #  /
  # 3 
  
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')

main()
