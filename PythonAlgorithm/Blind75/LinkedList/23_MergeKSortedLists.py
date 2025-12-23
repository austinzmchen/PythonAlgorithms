from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
# actually when tuple is given as input The comparator function will take the first attribute 
# to compare and if they are same it will go to for next attribute and so on if two values are same 
# it will throw "TypeError: unorderable types: Node() < Node()" error So to avoid that, 
# 2nd parameter i which will be unique in the tuple has been taken

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        min_heap = []
        i = 0 # used in tuple when preceding values are equal in heap
                
        for node in lists:
            if node:
                # this will error when val is equal, and node is not comparable
                heappush(min_heap, (node.val, i, node))
                i += 1

        dummy = ListNode()
        curr = dummy
        
        while min_heap:
            value, i, node = heappop(min_heap)
            curr.next = ListNode(value)
            
            node = node.next
            if node:
                heappush(min_heap, (node.val, i, node))
            curr = curr.next

        return dummy.next
      
      
lists = [ListNode(1), ListNode(1), ListNode(3)]
Solution().mergeKLists(lists)