import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        dp = [math.inf for _ in range(amount + 1)]

        for index in range(min(coins), amount + 1):
            if index in coins:
                dp[index] = 1
            else:
                for coin in coins:
                    if index - coin >= min(coins):
                        dp[index] = min(dp[index], dp[index - coin] + 1)
        return dp[-1] if dp[-1] != math.inf else -1