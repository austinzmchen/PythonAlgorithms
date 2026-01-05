from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_dict = {}

        for f in flights:
            a, b, cost = f

            adj_dict.setdefault(a, [])
            adj_dict[a].append((b, cost))
        
        import sys
        from functools import lru_cache

        @lru_cache
        def recur(num, stops, curr_cost):
            if stops < 0:
                return sys.maxsize
            if num == dst:
                return curr_cost
            
            min_cost = sys.maxsize
            for t in adj_dict.get(num, []):
                to, cost = t
                # print(f"{to=}, {cost=}")
                min_cost = min(min_cost, recur(to, stops - 1, cost + curr_cost))
            
            return min_cost
        
        res = recur(src, k + 1, 0)
        return -1 if res == sys.maxsize else res
    

print(Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))