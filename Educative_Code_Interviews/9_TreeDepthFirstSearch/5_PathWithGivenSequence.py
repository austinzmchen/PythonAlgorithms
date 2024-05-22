class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  return recur(root, sequence, 0)


def recur(root, sequence, idx):
  if root == None:
    return False

  if sequence[idx] != root.val:
    return False
  if root.left == None and root.right == None:
    return True

  return recur(root.left, sequence, idx + 1) or recur(root.right, sequence, idx + 1)


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
