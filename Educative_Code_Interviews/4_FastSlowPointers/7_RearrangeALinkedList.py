from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  slow, fast = head, head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

  head2 = reverse(slow)
  curr, curr2 = head, head2
  while curr != None and curr2 != None:
    next1 = curr.next
    next2 = curr2.next

    curr.next = curr2
    curr2.next = next1
    
    curr = next1
    curr2 = next2
  
  curr.next = None # need to end the loop cus curr.next points to self


def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
