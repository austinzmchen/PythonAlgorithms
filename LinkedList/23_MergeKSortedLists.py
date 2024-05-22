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
        _min = []
        i = 0
        from heapq import heappush, heappop
        for node in lists:
            if node:
                heappush(_min, (node.val, i, node))
                i += 1
        #
        new_head = ListNode(-1)
        curr = new_head
        while len(_min) > 0:
            item = heappop(_min)
            value, i, node = item
            curr.next = ListNode(value)
            curr = curr.next
            if node.next:
                heappush(_min, (node.next.val, i, node.next))
                i += 1
        #
        return new_head.next
      
      
lists = [ListNode(1), ListNode(1), ListNode(3)]
Solution().mergeKLists(lists)