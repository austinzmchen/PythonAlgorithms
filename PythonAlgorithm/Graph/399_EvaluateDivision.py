class Solution399:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        _dict = defaultdict(set)
        for i in range(0, len(equations)):
            eq = equations[i]
            v = values[i]
            _dict[eq[0]].add((eq[1], v))
            _dict[eq[1]].add((eq[0], 1/v))
        #
        res = []
        for j in range(0, len(queries)):
            q = queries[j]
            #
            visited = set()
            res.append(self.dfs(_dict, q[0], q[1], 1, visited))
        #
        return res
    
    def dfs(self, dict, source, target, num, visited):
        if source not in dict or source in visited:
            return -1.0
        if source == target:
            return num
        #
        for n in dict[source]:
            visited.add(source)
            r = self.dfs(dict, n[0], target, num * n[1], visited)
            visited.remove(source)
            if r != -1.0:
                return r
        #
        return -1.0
        