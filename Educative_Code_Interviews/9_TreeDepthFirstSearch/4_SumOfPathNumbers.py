class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    

def find_sum_of_path_numbers(root):
  res = 0
  
  def recur(node, sum):
    if not node:
      return

    nonlocal res
    if node.left is None and node.right is None:
      res += sum * 10 + node.val
      return

    recur(node.left, sum * 10 + node.val)
    recur(node.right, sum * 10 + node.val)
  #
  recur(root, 0)
  return res


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
  print("Total Sum of Path Numbers: " +
        str(find_sum_of_path_numbers(root)))
  # 332 = 101 + 116 + 115
  
main()
