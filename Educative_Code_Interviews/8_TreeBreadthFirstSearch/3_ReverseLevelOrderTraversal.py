from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  if root == None:
    return []

  result = []
  q = deque()
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

    result.insert(0, list)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
