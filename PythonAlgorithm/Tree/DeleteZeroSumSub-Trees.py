
class Solution:
  
  def delete_zero_sum_subtree(root):
    def recur(node):
      if not root:
        return 0
      left_sum = recur(node.left)
      right_sum = recur(node.right)
      if left_sum == 0:
        node.left = None
      if right_sum == 0:
        node.right = None
      return node.val + left_sum + right_sum
    #
    recur(root)

  