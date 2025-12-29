# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # merge sort
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        #
        prev.next = None
        list1 = self.sortList(head)
        list2 = self.sortList(slow)
        #
        new_dummy = ListNode(-1)
        curr = new_dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        #
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        #
        return new_dummy.next