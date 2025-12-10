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
  backward = False

  while deq:
    length = len(deq)
    level = []
    
    # per level
    for _ in range(length):
      node = deq.popleft()
      if node.left:
        deq.append(node.left)
      if node.right:
        deq.append(node.right)
        
      if backward:
        level.insert(0, node.val)
      else:
        level.append(node.val)
    #
    res.append(level)
    backward = not backward
  #
  return res


def main():
  # [12, 7, 1, 9, null, 10, 5, null, null, 20, 17, null, null]
  
  # Tree Structure:
  #        12
  #       / \
  #      7   1
  #     /   /  \
  #    9   10   5
  #       /  \
  #      20   17

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
