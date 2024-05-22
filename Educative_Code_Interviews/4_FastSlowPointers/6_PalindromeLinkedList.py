class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  slow, fast = head, head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

  head2 = reverse(slow)

  curr, curr2 = head, head2
  while curr != curr2:
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
