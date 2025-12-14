"""
Linked List Cycle (Fast & Slow Pointers Pattern)

Problem 1: Detect if a linked list has a cycle
Problem 2: Find the start of the cycle (if exists)
Problem 3: Calculate the length of the cycle

Examples:
    1 -> 2 -> 3 -> 4 -> 5 -> 6
              ^              |
              |______________|
    Has cycle: True
    Cycle start: Node 3
    Cycle length: 4

    1 -> 2 -> 3 -> 4 -> None
    Has cycle: False
"""


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# implement this func
def has_cycle(head):
  fast, slow = head, head
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: 
      break
  
  if fast and slow:
    # Step 2: Find cycle start
    # Reset slow to head, move both one step at a time
    slow = head
    while slow != fast:
      slow = slow.next
      fast = fast.next
    print(slow)  # This is the cycle start
    
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
    count += 1
    curr = curr.next
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