# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # inorder traversal on BST goes from small to big
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
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from heapq import heappush, heappop
        max_heap = []
        
        def recur(node):
            if not node:
                return
            
            recur(node.left)
            if len(max_heap) < k:
                heappush(max_heap, -node.val)
            else:
                if node.val < -max_heap[0]:
                   heappop(max_heap)
                   heappush(max_heap, -node.val)
            recur(node.right)

        recur(root)
        return -max_heap[0]