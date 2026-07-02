import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatBananas(rate):
            time = 0 
            for banana in piles:
                time += math.ceil(banana / rate)
            return time <= h 


        # We are looking for the first True (the first one that eats all the bananas within H)
        max_bananas = max(piles) # this is the upper bound -> eat at the rate of the highest banana in pile
        upper_bound = max_bananas
        lower_bound = 1
        current_rate = math.inf

        while lower_bound <= upper_bound:
            mid_rate = lower_bound + ((upper_bound - lower_bound) // 2)
            result = canEatBananas(mid_rate)
            # F T T T T T  -> format
            # If T, move to the left
            if result:
                current_rate = min(current_rate, mid_rate)
                upper_bound = mid_rate - 1
            # If F, move to the right
            else:
                lower_bound = mid_rate + 1

        return current_rate