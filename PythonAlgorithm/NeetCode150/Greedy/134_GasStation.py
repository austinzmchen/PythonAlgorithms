from typing import List

class Solution:
    
    # TLE
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for i in range(len(gas)):
            j, si = i, i
            curr_gas = gas[j]
            completed = False

            while curr_gas:
                curr_gas -= cost[j]
                if curr_gas < 0:
                    break
                
                # move to next station and wrap around
                j += 1
                if j == len(gas):
                    j = 0
                curr_gas += gas[j]

                if j == si:
                    completed = True
                    break
            
            if completed:
                return si
        
        return -1

    
    # Key Insight: If you can't reach station j from station i, then you also can't reach j from any station between i and j.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas < total cost, impossible
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            
            # If tank becomes negative, can't reach i+1 from start
            # So try starting from i+1
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
    
    
    # TLE
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        from functools import lru_cache
        @lru_cache
        def recur(idx, visited, curr_gas):
            curr_gas = curr_gas - cost[idx]
            if curr_gas < 0:
                return False

            if visited == len(gas):
                return True
            
            j = idx + 1
            if j > len(gas) - 1:
                j = 0
            
            return recur(j, visited + 1, curr_gas + gas[j])
        
        for i, g in enumerate(gas):
            if recur(i, 1, g):
                return i
        return -1
    

print(Solution().canCompleteCircuit([1,2,3,4,5], cost=[3,4,5,1,2]))
print(Solution().canCompleteCircuit([4,0,1], cost=[3,2,1]))
print(Solution().canCompleteCircuit([2,3,4], cost=[3,4,3]))
print(Solution().canCompleteCircuit([4,5,3,1,4], cost=[5,4,3,4,2]))