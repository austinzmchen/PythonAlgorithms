# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                n = queue.popleft()
                level.append(n.val)
                
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            res.append(level)
        return res
        