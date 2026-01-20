# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a or not b:
                return a == b
            
            return a.val == b.val and \
                    same(a.left, b.left) and \
                    same(a.right, b.right)

        def recur(node):
            if not node:
                return not subRoot
        
            return same(node, subRoot) or \
                    recur(node.left, subRoot) or \
                    recur(node.right, subRoot)
        
        return recur(root)