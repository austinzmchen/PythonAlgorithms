
def networkDelayTime(times, n, k):
    from collections import deque, defaultdict
    import sys
    
    # Build adjacency list
    graph = defaultdict(list)
    for frm, to, t in times:
        graph[frm].append((to, t))
    
    # Track minimum time to reach each node
    min_time = {i: sys.maxsize for i in range(1, n + 1)}
    min_time[k] = 0
    
    # BFS queue: (node, time_to_reach)
    queue = deque([(k, 0)])
    
    while queue:
        node, time = queue.popleft()
        
        # Skip if we've already found a better path to this node
        if time > min_time[node]:
            continue
        
        # Explore neighbors
        for nb, duration in graph[node]:
            new_time = time + duration
            
            # Only process if we found a shorter path
            if new_time < min_time[nb]:
                min_time[nb] = new_time
                queue.append((nb, new_time))
    
    # Get the maximum time (when the last node receives signal)
    max_time = max(min_time.values())
    
    # If any node is unreachable, return -1
    return -1 if max_time == sys.maxsize else max_time