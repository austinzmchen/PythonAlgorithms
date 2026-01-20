from collections import deque, defaultdict

class Solution:
    # TLE
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list and sort destinations
        adj_dict = defaultdict(list)
        for frm, to in tickets:
            adj_dict[frm].append(to)
        
        # Sort destinations for each source in lexicographical order
        for frm in adj_dict:
            adj_dict[frm].sort()
        
        # BFS: state = (current_airport, used_tickets_set, path)
        queue = deque([("JFK", frozenset(), ["JFK"])])
        total_tickets = len(tickets)
        
        while queue:
            airport, used, path = queue.popleft()
            
            # If we've used all tickets, return the path
            if len(used) == total_tickets:
                return path
            
            # Try each available ticket from current airport
            for i, destination in enumerate(adj_dict[airport]):
                # Create ticket identifier (source, dest, index in list)
                ticket_id = (airport, destination, i)
                
                # Check if this specific ticket hasn't been used
                if ticket_id not in used:
                    new_used = used | {ticket_id}
                    new_path = path + [destination]
                    queue.append((destination, new_used, new_path))
        
        return []  # Should not reach here for valid input