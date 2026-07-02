class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and word2:
            return len(word2)
        if word1 and not word2:
            return len(word1)
        if word1 == word2:
            return 0
        
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        for index in range(0, len(word1) + 1):
            dp[0][index] = index
        
        for index in range(0, len(word2) + 1):
            dp[index][0] = index
        
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        for row in dp:
            print(row)
        
        return dp[len(word2)][len(word1)]
