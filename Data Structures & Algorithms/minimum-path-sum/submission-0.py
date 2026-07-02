import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # You include the path you are on

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not (i == 0 and j == 0):
                    left = math.inf if (j == 0) else dp[i][j - 1] + grid[i][j]
                    top = math.inf if (i == 0) else dp[i - 1][j] + grid[i][j]
                    dp[i][j] = min(left, top)

        return dp[len(grid) - 1][len(grid[0]) - 1]