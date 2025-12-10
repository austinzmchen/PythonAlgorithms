class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.treeDiameter = 0

  def find_diameter(self, root) -> int:
    self.recur(root)
    return self.treeDiameter

  def recur(self, root):
    if not root:
      return 0

    left_depth = self.recur(root.left)
    right_depth = self.recur(root.right)

    self.treeDiameter = max(self.treeDiameter, left_depth + right_depth + 1)    
    return max(left_depth + 1, right_depth + 1)


def find_diameter(root) -> int:
  tree_diameter = 0
  
  def recur(node) -> int:
    if not node:
      return 0

    left_depth = recur(node.left)
    right_depth = recur(node.right)

    nonlocal tree_diameter
    tree_diameter = max(tree_diameter, left_depth + right_depth + 1)    
    
    return max(left_depth + 1, right_depth + 1)
  #
  recur(root)
  return tree_diameter
  
  
def main():
  # Tree Structure:
  #         1
  #       /   \
  #      2     3
  #    /      /  \
  #   4      5    6
  
  # treeDiameter = TreeDiameter()
  
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(find_diameter(root)))
  
  # Tree Structure:
  #         1
  #       /   \
  #      2      3
  #          /     \
  #         5       6
  #       /  \      /
  #      7    8    9
  #           /   /
  #         10   11
  
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(find_diameter(root)))

main()
