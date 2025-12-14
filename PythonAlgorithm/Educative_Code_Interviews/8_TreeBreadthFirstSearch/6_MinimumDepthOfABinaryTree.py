from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if not root:
    return 0

  deq = deque()
  deq.append(root)
  depth = 1

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
      
      if node.left is None and node.right is None:
        return depth
    #
    depth += 1
  #
  return depth


def main():
  # Tree Structure:
  #         12
  #       /    \
  #      7       1
  #    //\\     /  \
  #   9   11   10   5
  
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
