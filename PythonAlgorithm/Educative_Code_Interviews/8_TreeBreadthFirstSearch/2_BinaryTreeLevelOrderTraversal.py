#
# Problem Statement
# Given the root of a binary tree, return the level order traversal of its nodes' values 
# (i.e., from left to right, level by level).
#
# Examples
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
#
# Tree Structure:
#        3
#       / \
#      9  20
#        /  \
#       15   7
#
# Output: [[3], [9,20], [15,7]]
#
# Example 2:
# Input: root = [1]
# Output: [[1]]
#
# Example 3:
# Input: root = []
# Output: []
#

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  if not root: 
    return []

  res = []
  deq = deque() # double ended queue
  deq.append(root)

  while deq:
    length = len(deq)
    level = []
    for _ in range(length):
      node = deq.popleft()
      level.append(node.val)
      
      if node.left:
        deq.append(node.left)
      if node.right:
        deq.append(node.right)
    #
    res.append(level)
  #
  return res


def main():
  # [12, 7, 1, 9, null, 10, 5]
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
