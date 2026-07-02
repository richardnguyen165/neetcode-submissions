class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Combining from 1 step or 2 step before
        dp = [0 for _ in range(n + 1)]
        
        # From the one step before, get all the possibilites and add one step
        # From the two step before, get all the possibilites and add two step
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]