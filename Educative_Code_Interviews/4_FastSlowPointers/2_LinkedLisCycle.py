class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  fast, slow = head, head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: 
      return True

  return False


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()

#####


def find_cycle_length(head):
  fast, slow = head, head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: 
      return calculate_cycle_length(slow)

  return 0


def calculate_cycle_length(head):
  curr = head
  count = 1
  while curr.next != head:
    curr = curr.next
    count += 1

  return count


def main2():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main2()