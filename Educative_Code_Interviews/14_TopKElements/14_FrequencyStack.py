# Problem Statement
# Leetcode: 895. Maximum Frequency Stack
# Design a stack-like data structure that pops the most frequent element. If there's a tie, pop the element closest to the top of the stack.

# Example Walkthrough
# Operations: push(5), push(7), push(5), push(7), push(4), push(5)
# State after pushes:

# Frequencies: {5: 3, 7: 2, 4: 1}
# Groups: {1: [4], 2: [7, 7], 3: [5, 5, 5]}

# Pop sequence:

# pop() → 5 (freq 3, most recent)
# pop() → 7 (freq 2, most recent)
# pop() → 5 (freq 2, most recent)
# pop() → 7 (freq 1, most recent)

from heapq import heappop, heappush

class FreqStack:
    """
    Stack that pops the most frequent element.
    If tie, pops the element closest to the top.
    """
    
    # max_heap stores every push, so multiple of `5` is 5 is pushed as many times
    
    def __init__(self):
        self.freq = {}  # Element -> frequency
        self.max_heap = []  # Max heap: (-frequency, -timestamp, value)
        self.timestamp = 0  # Tracks insertion order
    
    def push(self, val: int) -> None:
        """Push value onto the stack."""
        self.timestamp += 1
        self.freq[val] = self.freq.get(val, 0) + 1
        
        # Push to max heap with negative values for max behavior
        # Format: (-frequency, -timestamp, value)
        heappush(self.max_heap, (-self.freq[val], -self.timestamp, val))
    
    def pop(self) -> int:
        """Pop the most frequent element (most recent if tie)."""
        # Pop from heap
        freq, ts, val = heappop(self.max_heap)
        
        # Decrement frequency
        self.freq[val] -= 1
        return val
    
    
def main():
    stack = FreqStack()
    stack.push(5);stack.push(7);stack.push(5);stack.push(7);stack.push(4);stack.push(5)
    
    print("FreqStack:  " + str(stack.pop()))
    print("FreqStack:  " + str(stack.pop()))
    print("FreqStack:  " + str(stack.pop()))
    print("FreqStack:  " + str(stack.pop())) # pop 4, which has 1, but most recent

main()