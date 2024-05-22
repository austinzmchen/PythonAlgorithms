# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_depth, y_depth = -1, -1
        x_parent, y_parent = None, None
        #
        def recur(node, depth, parent):
            if not node:
                return
            #
            nonlocal x_depth, y_depth, x_parent, y_parent
            if node.val == x:
                x_depth = depth
                x_parent = parent
            elif node.val == y:
                y_depth = depth
                y_parent = parent
            #
            recur(node.left, depth + 1, node)
            recur(node.right, depth + 1, node)
            return
        #
        recur(root, 0, None)
        return x_depth == y_depth and (x_parent is not y_parent)