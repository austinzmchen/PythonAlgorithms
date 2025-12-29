from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        results = [0] * n
        #
        stack = []
        curr_f: int = None
        curr_t = 0
        for log in logs:
            func, is_start, time = log.split(':')
            t = int(time)
            if is_start == 'start':
                if curr_f != None:
                    results[curr_f] += t - curr_t
                    stack.append(curr_f)
                #
                curr_f = int(func)
                curr_t = t
            else:
                results[int(func)] += t + 1 - curr_t
                curr_t = t + 1
                if len(stack) > 0:
                  curr_f = stack.pop()
            #
        #
        return results
      
      
print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))