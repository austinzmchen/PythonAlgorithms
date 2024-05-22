from typing import Deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if root == None:
    return 0

  q = Deque()
  q.append(root)
  depth = 1

  while len(q) > 0:
    length = len(q)
    list = []
    for i in range(length):
      node = q.popleft()
      list.append(node.val)

      if node.left == None and node.right == None:
        return depth
      if node.left != None:
        q.append(node.left)
      if node.right != None:
        q.append(node.right)

    depth += 1

  return depth


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
