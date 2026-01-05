# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def recur(node, depth):
            if not node:
                return
            
            if len(res) < depth + 1:
                res.append(node.val)

            recur(node.left, depth + 1)
            recur(node.right, depth + 1)

            if depth < len(res):
                res[depth] = node.val

        recur(root, 0)
        return res