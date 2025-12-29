# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder array has left nodes on the left of the root, 
        # and right nodes on the right of the root, 
        # thus good for recurisive call with range (left & right)
        
        _dict = {v:i for i,v in enumerate(inorder)}
        p_i = 0
        
        def recur(l, r):
            if l > r:
                return None
            
            nonlocal p_i
            v = preorder[p_i]
            root = TreeNode(v)
            p_i += 1
            
            root.left = recur(l, _dict[v] - 1)
            root.right = recur(_dict[v] + 1, r)
            return root

        return recur(0, len(inorder) - 1)
            