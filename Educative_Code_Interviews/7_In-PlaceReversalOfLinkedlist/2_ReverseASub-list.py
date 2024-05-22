from __future__ import print_function
import sys
from typing import List, Tuple


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


def reverse_sub_list(head, p, q):
  p_before = None
  q_node = None
  dummy = Node(sys.maxsize, next=head)

  prev = None
  curr = head
  while curr != None:
    if curr.value == p:
      p_before = prev
    elif curr.value == q:
      q_node = curr

    prev = curr
    curr = curr.next

  q_after = q_node.next
  rev_list_head, rev_list_tail = reverse(p_before.next, q_node)
  p_before.next = rev_list_head
  rev_list_tail.next = q_after
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

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()