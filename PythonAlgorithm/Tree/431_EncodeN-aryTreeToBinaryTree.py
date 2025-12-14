# https://walkccc.me/LeetCode/problems/0431/
class Codec:
  # Encodes an n-ary tree to a binary tree.
  def encode(self, root: 'Node') -> Optional[TreeNode]:
    if not root:
      return
    new_node = TreeNode(root.val)
    if root.children:
      new_node.left = self.encode(root.children[0])
    #
    curr_node = new_node
    for i in range(1, len(root.children)):
      curr_node.right = self.encode(root.children[i])
      curr_node = curr_node.right
    #
    return new_node
    
  # Decodes your binary tree to an n-ary tree.
  def decode(self, root: Optional[TreeNode]) -> 'Node':
    if not root:
      return
    new_node = Node(root.val)
    #
    curr_node = root.left
    while curr_node:
      new_node.children.append(self.decode(curr_node))
      curr_node = curr_node.right
    return new_node