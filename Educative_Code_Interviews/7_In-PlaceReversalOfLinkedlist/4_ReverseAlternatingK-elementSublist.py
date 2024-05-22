from __future__ import print_function
from typing import Tuple


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_alternate_k_elements(head, k):
  import sys
  dummy = Node(sys.maxsize, head)
  prev, curr = dummy, dummy
  skip = True

  while True:
    i = 0
    while i < k and curr != None:
      curr = curr.next
      i += 1
    
    if curr == None:
      break
    
    if skip:
      curr_next = curr.next
      new_head, new_tail = reverse(prev.next, curr)
      prev.next = new_head
      new_tail.next = curr_next

      prev, curr = new_tail, new_tail
    else:
      prev = curr

    skip = not skip

  return dummy.next


def reverse(p_node, q_node) -> Tuple:
  prev = None
  curr = p_node
  end = q_node.next

  while curr != end:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

  return (q_node, p_node)

  
def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
