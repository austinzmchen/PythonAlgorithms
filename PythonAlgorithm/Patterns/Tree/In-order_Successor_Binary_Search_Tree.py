
class Solution:
  # The in-order successor of a node is the left-most node in its right sub-tree, if exists. 
  # If not, then it is the root of the smallest left sub-tree this node is in.
  def find_inorder_successor(root, node_value):
    prev = None
    curr = root
    while curr:
      if node_value < curr.val:
        prev = curr
        curr = curr.left
      else: # if equal, still need to proceed to find the smallest left node
        curr = curr.right
    return prev