from __future__ import print_function
import sys
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


def reverse_every_k_elements(head, k):
  dummy = Node(sys.maxsize, next=head)
  p_before = dummy

  prev = None
  curr = head
  count = 0

  while curr != None:
    prev = curr
    curr = curr.next
    count += 1

    if count == k:
      rev_list_head, rev_list_tail = reverse(p_before.next, prev)
      p_before.next = rev_list_head
      rev_list_tail.next = curr
      p_before = rev_list_tail
      count = 0


  rev_list_head, rev_list_tail = reverse(p_before.next, prev)
  p_before.next = rev_list_head
  rev_list_tail.next = curr
  p_before = rev_list_tail

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
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

