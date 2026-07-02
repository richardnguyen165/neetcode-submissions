class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        left_pointer, current, profit = 0, 0, 0
        for right_pointer in range(1, len(prices)):
            difference = prices[right_pointer] - prices[left_pointer]
            while difference < 0 and left_pointer != right_pointer:
                left_pointer += 1
                difference = prices[right_pointer] - prices[left_pointer]
            profit = max(difference, profit)
        return profit
