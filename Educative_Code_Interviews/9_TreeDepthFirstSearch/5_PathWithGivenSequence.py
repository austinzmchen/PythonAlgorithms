class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  def recur(node, idx):
    if not node:
      return False

    if sequence[idx] != node.val:
      return False
    if node.left == None and node.right == None:
      return True

    return recur(node.left, idx + 1) or \
          recur(node.right, idx + 1)
  #
  return recur(root, 0)


def main():
  # Tree Structure:
  #         1
  #       /   \
  #      0     1
  #    /      /  \
  #   1      6    5
  
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
