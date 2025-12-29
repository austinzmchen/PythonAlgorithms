from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if not root:
    return []

  deq = deque()
  deq.append(root)
  flag = False
  
  while deq:
    length = len(deq)
    
    for _ in range(length):
      node = deq.popleft()
      
      if flag:
        return node
      elif node.val == key:
        flag = True

      if node.left:
        deq.append(node.left)
      if node.right:
        deq.append(node.right)
  #
  return None


def main():
  # Tree Structure:
  #        12
  #       /   \
  #      7     1
  #    /      /  \
  #   9      10   5
  
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = find_successor(root, 12)
  if result:
    print(result.val)
    
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
