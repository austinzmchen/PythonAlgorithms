from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  if not root:
    return []

  res = []
  deq = deque()
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
    res.insert(0, level)
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
  print("Reverse level order traversal: " + str(traverse(root)))


main()
