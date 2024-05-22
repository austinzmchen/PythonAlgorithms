
from collections import deque
from threading import Semaphore

class BoundedBlockingQueue:
  
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.deque = deque(maxlen=capacity)
    self.sem_enq = Semaphore(capacity)
    self.sem_deq = Semaphore(0)
    
  def enqueue(self, element: int):
    self.sem_enq.acquire()
    self.deque.append(element)
    self.sem_deq.release()
    
  def dequeue(self) -> int:
    self.sem_deq.acquire()
    r = self.deque.popleft()
    self.sem_enq.release()
    return r
  
  def size(self) -> int:
    return len(self.deque)