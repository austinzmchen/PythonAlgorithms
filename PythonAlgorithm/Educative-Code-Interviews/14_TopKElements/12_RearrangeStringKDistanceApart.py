# Problem Description
# Given a string s and an integer k, rearrange the string such that the same characters are at least distance k apart from each other. If it's not possible, return an empty string.

# Examples:
# Input: s = "aabbcc", k = 3
# Output: "abcabc" (or "abacbc", "bacbac", etc.)
# Explanation: The same letters are at least distance 3 from each other

# Input: s = "aaabc", k = 3
# Output: ""
# Explanation: Not possible - we have 3 'a's but can't space them 3 apart

# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd" (or similar valid arrangements)

from heapq import heappop, heappush
from collections import deque

# not working
def rearrange_string_2(s: str, k: int) -> str:
    freq_dict = {}
    for c in s:
        freq_dict[c] = freq_dict.setdefault(c, 0) + 1
    
    max_heap = []
    for c, freq in freq_dict.items():
        heappush(max_heap, (-freq, c))
    
    queue = deque() # cool down queue
    res = []
    
    while max_heap:
        # Get character with highest frequency
        freq, c = heappop(max_heap)
        res.append(c)
        
        # add to cooldown queue, without check freq yet
        queue.append((-freq-1, c))
        
        # check the cooldown queue chars that are ready to re-use
        if len(queue) >= k:
            f, c = queue.popleft()
            if f > 0:
                heappush(max_heap, (-f, c))
    
    # Return result if all characters placed, otherwise empty string
    return ''.join(res) if len(s) == len(res) else ""


def rearrange_string(s: str, k: int) -> str:
    freq_dict = {}
    for c in s:
        freq_dict[c] = freq_dict.setdefault(c, 0) + 1
    
    max_heap = []
    for c, freq in freq_dict.items():
        heappush(max_heap, (-freq, c))
    
    queue = deque()
    res = []
    time = 0
        
    while max_heap or queue:
        # If queue reaches size k, check if first character can be reused
        if queue and queue[0][2] == time:
            f, c, _ = queue.popleft()
            heappush(max_heap, (-f, c))
        
        if max_heap:
            # Get character with highest frequency
            freq, c = heappop(max_heap)
            res.append(c)
            
            if -freq - 1 > 0:
                # add next available time
                queue.append((-freq-1, c, time + k))
        else:
            return ""

        time += 1        
    # Return result if all characters placed, otherwise empty string
    return "".join(res)


def main():
  print("Rearranged string:  " + rearrange_string("aabbcc", 3))
  print("Rearranged string:  " + rearrange_string("aaabc", 3))
  print("Rearranged string:  " + rearrange_string("aaadbbcc", 2))

main()