from typing import Deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  if root == None:
    return []

  result = []
  q = Deque()
  q.append(root)

  while len(q) > 0:
    length = len(q)
    list = []
    for i in range(length):
      node = q.popleft()
      list.append(node.val)
      if node.left != None:
        q.append(node.left)
      if node.right != None:
        q.append(node.right)

    result.append(sum(list) / len(list))

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()
