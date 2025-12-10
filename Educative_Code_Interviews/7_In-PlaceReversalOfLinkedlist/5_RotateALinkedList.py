# Problem Statement
# Given a linked list and a number k, rotate the linked list to the right by k places.

# Examples
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: 4 -> 5 -> 1 -> 2 -> 3
#
# Explanation: 
# Rotate 1: 5 -> 1 -> 2 -> 3 -> 4
# Rotate 2: 4 -> 5 -> 1 -> 2 -> 3

# Example 2:
# Input: 1 -> 2 -> 3, k = 4
# Output: 3 -> 1 -> 2
#
# Explanation: k = 4 is same as k = 1 (since 4 % 3 = 1)
#

from __future__ import print_function

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


def rotate(head, rotations):
  dummy = Node(0, next=head)

  tail = dummy
  length = 0
  while tail.next != None:
    tail = tail.next
    length += 1

  # Explanation: k = 4 is same as k = 1 (since 4 % 3 = 1)
  rots = rotations % length
  count = length - rots
  
  curr = dummy
  for i in range(count):
    curr = curr.next

  new_head = curr.next
  curr.next = None
  tail.next = head

  return new_head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()
