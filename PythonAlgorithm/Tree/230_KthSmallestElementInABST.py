# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, res = 0, -1
        
        def recur(node):
            if not node:
                return
            
            nonlocal count, res
            
            recur(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            recur(node.right)

        recur(root)
        return res
    
      
"""
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and 
    you need to find the kth smallest frequently, how would you optimize?

    Check the new value is bigger or smaller than the top of the max_heap, and decide to add
"""  

class Solution:
    def __init__(self):
        self.max_heap = [] # of size k
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def recur(node):
            if not node:
                return
            
            recur(node.left)
            if len(self.max_heap) < k:
                heappush(self.max_heap, -node.val)
            recur(node.right)

        recur(root)
        return -self.max_heap[0]