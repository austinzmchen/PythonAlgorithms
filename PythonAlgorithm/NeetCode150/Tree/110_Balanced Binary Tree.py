# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def recur(node, depth):
            if not node:
                return depth
            
            left = recur(node.left, depth + 1)
            right = recur(node.right, depth + 1)

            nonlocal res
            if abs(left - right) > 1:
                res = False

            return max(left, right)
        
        recur(root, 0)
        return res
    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def recur(node):
            if not node:
                return 0
            
            left = recur(node.left)
            right = recur(node.right)

            if abs(left - right) > 1:
                nonlocal res
                res = False

            return max(left, right) + 1
        
        recur(root)
        return res