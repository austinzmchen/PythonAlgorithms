"""
Palindrome Linked List (Fast & Slow Pointers Pattern)

Problem:
Given the head of a singly linked list, determine if it's a palindrome.
A palindrome reads the same forwards and backwards.

Examples:
    Input: 2 -> 4 -> 6 -> 4 -> 2
    Output: True (palindrome)

    Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2
    Output: False (not palindrome)

    Input: 1
    Output: True (single element is palindrome)

    Input: 1 -> 2
    Output: False
    
    Input: 1 -> 1
    Output: True
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  # find middle of linked list
  slow, fast = head, head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

  head2 = reverse(slow)

  curr, curr2 = head, head2
  while curr != curr2: # both would meet in the middle node
    if curr.value != curr2.value:
      reverse(head2) # reverse back
      return False
    
    curr = curr.next
    curr2 = curr2.next

  reverse(head2)  # reverse back
  return True


def reverse(head):
  prev = None
  curr = head
  while curr != None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev


def is_palindromic_linked_list_2(head):
  # find middle of linked list
  slow, fast = head, head
  count = 0
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
    count += 1

  head2 = reverse_copy(slow)

  curr, curr2 = head, head2
  while count > 0:
    if curr.value != curr2.value:
      return False
    curr = curr.next
    curr2 = curr2.next
    count -= 1

  return True


def reverse_copy(head):
  curr = head
  prev_new = None
  while curr != None:
    new = Node(curr.value)
    new.next = prev_new
    
    prev_new = new
    curr = curr.next
  return prev_new


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
