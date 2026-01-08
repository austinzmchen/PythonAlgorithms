class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        from heapq import heappush, heappop, heapify
        
        counter = Counter(tasks) # like freq dict
        # use max heap to get most frequent char
        max_heap = [(-freq, c, 0) for c, freq in counter.items()]
        heapify(max_heap)
        
        time = 0
        cool_q = deque()
        
        while max_heap or cool_q:
            if cool_q:
                f, c, t = cool_q[0]
                if time == t:
                    cool_q.popleft()
                    heappush(max_heap, (-f, c, t))
                    
            if max_heap:
                freq, c, _ = heappop(max_heap)
                
                if -freq - 1 > 0:
                    cool_q.append((-freq-1, c, time + n + 1))
                    
            time += 1
        
        return time