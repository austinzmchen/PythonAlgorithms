class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class SumOfPathNumbers:
  def __init__(self) -> None:
    self.res = 0

  def find_sum_of_path_numbers(self, root):
    self.recur(root, 0)
    return self.res

  def recur(self, root, sum):
    if root == None:
      return

    if root.left == None and root.right == None:
      self.res += sum * 10 + root.val
      return

    self.recur(root.left, sum * 10 + root.val)
    self.recur(root.right, sum * 10 + root.val)
  


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " +
        str(SumOfPathNumbers().find_sum_of_path_numbers(root)))


main()
