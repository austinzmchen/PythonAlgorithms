# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        #
        q = [root]
        r = []
        while len(q) > 0:
            ls = []
            size = len(q)
            for _ in range(size):
                n = q.pop(0)
                ls.append(n.val)
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
            #
            r.append(ls)
        #
        return r
        