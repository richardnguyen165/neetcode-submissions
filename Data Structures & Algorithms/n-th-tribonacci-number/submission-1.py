class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0 for  _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for index in range(3, len(dp)):
            dp[index] = dp[index - 1] + dp[index - 2] + dp[index - 3]
        print(dp)
        return dp[-1]