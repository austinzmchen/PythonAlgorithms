class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_dict = {}
        in_degrees = {}
        for i in range(numCourses):
            adj_dict[i] = []
            in_degrees[i] = 0
            
        for req in prerequisites:
            curr, pre = req
            adj_dict[pre].append(curr)
            in_degrees[curr] += 1
        
        queue = []
        for i, v in in_degrees.items():
            if v == 0:
                queue.append(i)
        
        if not queue:
            return []
        
        res = []
        while queue:
            course = queue.pop(0)
            res.append(course)
            
            for adj in adj_dict[course]:
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    queue.append(adj)
            
        return res if len(res) == numCourses else []