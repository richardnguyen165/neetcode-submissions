class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if not (i == 0 and j == 0):
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0

                    top = 0 if (i == 0 or obstacleGrid[i - 1][j] == 1) else dp[i - 1][j]
                    left = 0 if (j == 0 or obstacleGrid[i][j - 1] == 1) else dp[i][j - 1]

                    dp[i][j] = top + left

        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]