
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]

        # sort desc so that closest to the target comes first, 
        #   because behind cars can not pass front cars
        cars.sort(reverse=True)
        time = 0
        res = 0
        
        for p, s in cars:
            arrival_time = (target - p) / s
            
            if arrival_time > time:
                res += 1
                time = arrival_time
        
        return res            
        
    
print(Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))