from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # Count frequency of each card
        from collections import Counter
        count = Counter(hand)

        # Process cards in sorted order
        for card in sorted(count.keys()):
            freq = count[card]

            if freq == 0:
                continue
            
            # Need to form 'freq' groups starting with 'card'
            for i in range(groupSize):
                if count[card + i] < freq:
                    # Not enough cards to form the groups
                    return False
                count[card + i] -= freq
        
        return True