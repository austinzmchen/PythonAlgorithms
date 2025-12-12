# Problem Statement
# Given an array of tasks (represented by characters) and a cooldown period n, 
# find the minimum time needed to complete all tasks. The same task must wait at least n intervals before it can be executed again.

from heapq import heappop, heappush
from collections import deque

def schedule_tasks(tasks: list[str], k: int) -> int:
    # Count frequency of each task
    freq_dict = {}
    for c in tasks:
        freq_dict[c] = freq_dict.setdefault(c, 0) + 1
    
    # Create max heap with WaitItem objects
    max_heap = []
    for char, freq in freq_dict.items():
        heappush(max_heap, (-freq, char, -1))
    
    time = 0
    queue = deque()
    
    while max_heap or queue:
        # Check if any task in queue can be released from cooldown
        if queue and queue[0][2] == time:
            f, c, i = queue.popleft()
            heappush(max_heap, (-f, c, i))
            
        # Execute a task if available
        if max_heap:
            freq, char, _ = heappop(max_heap)
            
            # If task still has remaining executions
            if -freq - 1 > 0:
                queue.append((-freq-1, char, time + k + 1))
        
        time += 1
    return time


def main():
  print("Scheduling tasks:  " + str(schedule_tasks(['A','A','A','B','B','B'], 2)))

main()