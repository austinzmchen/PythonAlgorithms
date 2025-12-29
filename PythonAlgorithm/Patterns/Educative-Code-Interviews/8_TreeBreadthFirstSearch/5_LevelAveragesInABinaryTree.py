from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  if not root:
    return []

  res = []
  deq = deque()
  deq.append(root)

  while len(deq) > 0:
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
    res.append(sum(level) / len(level))
  #
  return res


def main():
  # Tree Structure:
  #        12
  #       /   \
  #      7     1
  #    / \    /  \
  #   9   2  10   5
  
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()
