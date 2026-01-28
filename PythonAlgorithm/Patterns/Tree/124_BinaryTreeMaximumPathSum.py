# Definition for a binary tree node.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        import sys
        res = -sys.maxsize-1
        
        def recur(node):
            if not node:
                return 0
            
            nonlocal res
            left = recur(node.left)
            right = recur(node.right)
            
            res = max(res, node.val,
                       left + right + node.val, 
                       left + node.val,
                       right + node.val)

            return max(node.val, 
                       left + node.val, 
                       right + node.val)

        recur(root)
        return res