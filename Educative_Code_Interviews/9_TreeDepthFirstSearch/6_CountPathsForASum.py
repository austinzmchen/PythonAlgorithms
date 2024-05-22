class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  path = []
  return recur(root, path, S, 0)

def recur(root, path, sum, count) -> int:
  if root == None:
    return 0
  
  path.append(root.val)

  curr_count = count
  curr_sum = 0
  for i in range(len(path) - 1, -1, -1):
    curr_sum += path[i]
    if curr_sum == sum:
      curr_count += 1

  curr_count += recur(root.left, path, sum, curr_count) + \
      recur(root.right, path, sum, curr_count)

  del path[-1]
  return curr_count


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
