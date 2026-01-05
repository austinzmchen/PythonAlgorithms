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
    

print(Solution().canCompleteCircuit([1,2,3,4,5], cost=[3,4,5,1,2]))
print(Solution().canCompleteCircuit([4,0,1], cost=[3,2,1]))