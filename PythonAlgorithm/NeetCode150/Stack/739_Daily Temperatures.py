class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        stack = deque()
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            stack.append(i)

        return res