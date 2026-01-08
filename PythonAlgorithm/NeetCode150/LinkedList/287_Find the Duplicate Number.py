class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hashset solution is easy
        pass
    
    # fast and slow pointer like in linked list
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # now start anew to meet at the looping intersection
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow