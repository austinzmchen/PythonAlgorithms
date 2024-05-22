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
  import sys
  dummy = Node(sys.maxsize)
  dummy.next = head

  tail = dummy
  length = 0
  while tail.next != None:
    tail = tail.next
    length += 1

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
