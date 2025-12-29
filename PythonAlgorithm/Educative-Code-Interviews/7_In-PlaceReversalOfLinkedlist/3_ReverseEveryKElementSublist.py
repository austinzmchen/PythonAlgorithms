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


def reverse_every_k_elements_1(head, k):
  dummy = Node(0, next=head)
  p_before = dummy

  prev = None
  curr = head
  count = 0
  
  def update_inplace():
    nonlocal p_before, prev
    
    new_head, new_tail = reverse(p_before.next, prev)
    p_before.next = new_head
    new_tail.next = curr
    
    p_before = new_tail
    
  while curr != None:
    prev = curr
    curr = curr.next
    count += 1

    if count == k:
      update_inplace() 
      count = 0
  #
  update_inplace()
  
  return dummy.next


def reverse_every_k_elements(head, k):
  dummy = Node(0, next=head)
  
  p_before = dummy
  count = 1
  
  prev = None
  curr = head
  
  def update_inplace(end_node):
    nonlocal p_before
    #
    curr_next = end_node.next
    new_head, new_tail = reverse(p_before.next, end_node)
    p_before.next = new_head
    new_tail.next = curr_next
    p_before = new_tail
    
  while curr != None:
    if count == k:
      curr_next = curr.next
      update_inplace(curr)
      
      prev = p_before
      curr = curr_next
      count = 1
    
    else:
      prev = curr
      curr = curr.next
      count += 1

  # now curr is None, reverse the rest
  update_inplace(prev)
  
  return dummy.next


def reverse(p_node, q_node) -> tuple:
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

