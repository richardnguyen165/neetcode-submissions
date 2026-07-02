class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        left_pointer, current, profit = 0, 0, 0
        # move right to the right, start at 2 since you cant start on same day
        for right_pointer in range(1, len(prices)):
            difference = prices[right_pointer] - prices[left_pointer]
            # meaning, move left pointer to the right, and find the next price, until we get neutral or positive profit
            while difference < 0 and left_pointer != right_pointer:
                left_pointer += 1
                difference = prices[right_pointer] - prices[left_pointer]
            # max it
            profit = max(difference, profit)
        return profit
