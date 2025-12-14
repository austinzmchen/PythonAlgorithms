class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_dict = {}
        in_degrees = {}
        for i in range(numCourses):
            adj_dict[i] = []
            in_degrees[i] = 0
            
        for pair in prerequisites:
            adj_dict[pair[1]].append(pair[0])
            in_degrees[pair[0]] += 1
        
        queue = []
        for i, v in in_degrees.items():
            if v == 0:
                queue.append(i)
        
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