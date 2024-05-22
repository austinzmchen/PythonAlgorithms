from __future__ import print_function
from heapq import *
import sys


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None
  
  def __lt__(self, other):
    return self.value < other.value


def merge_lists(lists):
  dummy_head = ListNode(sys.maxsize)
  curr = dummy_head

  min_heap = []
  for n in lists:
    heappush(min_heap, n)

  while len(min_heap) > 0:
    node = heappop(min_heap)
    curr.next = node
    curr = curr.next
    if node.next != None:
      heappush(min_heap, node.next)

  return dummy_head.next


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()
