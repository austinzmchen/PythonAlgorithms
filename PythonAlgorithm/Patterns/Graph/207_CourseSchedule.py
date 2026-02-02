
class Solution:
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_dict = {}
        in_degrees = {}
        for i in range(numCourses):
            adj_dict[i] = []
            in_degrees[i] = 0

        for req in prerequisites:
            curr, pre = req
            adj_dict[pre].append(curr)
            in_degrees[curr] += 1
        
        queue = [i for i, v in in_degrees.items() if v == 0]
        if not queue:
            return False
        
        res = set()
        while queue:
            course = queue.pop(0)
            res.add(course)
            
            for adj in adj_dict[course]:
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    queue.append(adj)
            
        return len(res) == numCourses
    
    
    # Not working! 1 courses can map to multiple other courses
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        _dict = {}
        for req in prerequisites:
            curr, pre = req
            _dict[curr] = pre
        print(f"{_dict=}")
        
        def recur(n, visited):
            if n in visited:
                return False
            
            print(f"recur {n=}, {visited=}")
            visited.add(n)
            
            if (pre := _dict.get(n)) is not None:
                return recur(pre, visited)
            return True

        can_finish = True
        for i in range(numCourses):
            can_finish = can_finish and recur(i, set())
        
        return can_finish
    

print(Solution().canFinish(3, [[1,0],[1,2],[0,1]]))