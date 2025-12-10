
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeMax:
  def __init__(self):
    import sys
    self.tree_max = -sys.maxsize-1

  def find_maximum_path_sum(self, root) -> int:
    self.recur(root)
    return self.tree_max

  def recur(self, root):
    if not root:
      return 0

    left_depth = self.recur(root.left)
    right_depth = self.recur(root.right)

    self.tree_max = max(root.val, self.tree_max, left_depth + right_depth + root.val)
    return max(left_depth + root.val, right_depth + root.val)


def find_maximum_path_sum(root) -> int:
  import sys
  res = -sys.maxsize-1
  
  def recur(node) -> int:
    if not node:
      return 0

    left_v = recur(node.left)
    right_v = recur(node.right)

    nonlocal res
    # max 3 numbers because there could be negative value
    res = max(res, node.val, left_v + right_v + node.val)
    return max(left_v + node.val, right_v + node.val)

  recur(root)
  return res


def main():
  # Tree Structure:
  #           1
  #       /        \
  #      2          3
  #     / \       /   \
  #    1   3    5      6
  #            / \     /
  #           7   8   9
  
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
  
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

main()
