
# https://zhenyu0519.github.io/2020/03/13/lc545/
def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
  if not root:
    return []
  results = [root.val]
  # pre-order
  def left_recur(node):
    if not node or not node.left and not node.right:
      return
    results.append(node.val)
    if node.left:
      left_recur(node.left)
    elif node.right:
      left_recur(node.right)
  #
  def leaf_recur(node):
    if not node:
      return
    if (not node.left and not node.right) and \
        node is not root: # case root is the only node in the tree
      results.append(node.val)
    leaf_recur(node.left)
    leaf_recur(node.right)
  # post-order
  def right_recur(node):
    if not node or not node.left and not node.right:
      return
    if node.right:
      right_recur(node.right)
    elif node.left:
      right_recur(node.left)
    results.append(node.val)
  #
  left_recur(root.left)
  leaf_recur(root)
  right_recur(root.right)
  return results
      