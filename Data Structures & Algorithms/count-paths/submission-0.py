class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = 1
                else:
                    total = dp[i - 1][j]
                    if j != 0:
                        total += dp[i][j - 1]
                    dp[i][j] = total
        
        return dp[m - 1][n - 1]