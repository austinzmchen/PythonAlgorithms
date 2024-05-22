# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def recur(root):
            nonlocal res
            if root == None:
                return 0
            found = 0
            found += recur(root.left)
            found += recur(root.right)
            if root == p or root == q:
                found += 1
            if found == 2:
                res = root
                return 0
            return found
        
        recur(root)
        return res