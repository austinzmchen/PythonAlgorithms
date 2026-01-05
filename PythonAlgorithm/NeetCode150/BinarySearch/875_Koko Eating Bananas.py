import math

# Solution 1: Binary Search (Optimal) ⭐
# The key insight: if Koko can eat all bananas at speed k, she can also do it at any speed > k. This monotonic property makes binary search perfect!

def minEatingSpeed(piles: list[int], h: int) -> int:
    def can_finish(speed):
        hours = sum(math.ceil(pile / speed) for pile in piles)
        return hours <= h
    
    left = 1 # Minimum possible speed
    right = max(piles) # Maximum needed speed (eat largest pile in 1 hour)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_finish(mid):
            # Can finish with this speed, try slower
            right = mid
        else:
            # Too slow, need faster speed
            left = mid + 1
    
    # return left because left can finish
    return left