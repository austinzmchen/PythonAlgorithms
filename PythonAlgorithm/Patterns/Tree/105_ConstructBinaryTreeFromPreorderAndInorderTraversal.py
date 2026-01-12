# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # - inorder array has left nodes on the left of the root, and right nodes on the right of the root, 
    #       thus good for recurisive call with range (left & right)
    #
    # - Use preorder array to build the nodes
    # - Use inorder array to see where to stop
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        _dict = {n:i for i, n in enumerate(inorder)}
        pi = 0
        
        def recur(l, r):
            if l > r:
                return None
            
            nonlocal pi
            n = preorder[pi]
            root = TreeNode(n)
            pi += 1
            
            root.left = recur(l, _dict[n] - 1)
            root.right = recur(_dict[n] + 1, r)
            return root

        return recur(0, len(inorder) - 1)