class Solution:
    def countSubstrings(self, s: str) -> int:
        number_of_substrings = 0

        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                # Handles case with one letter
                if i == j:
                    dp[i][i] = True
                    number_of_substrings += 1 

                # Two letter
                elif j == i + 1:
                    dp[i][j] = s[i] == s[j]
                    number_of_substrings = number_of_substrings + 1 if s[i] == s[j] else number_of_substrings 

                # > 2
                else:
                    if dp[i + 1][j - 1] and s[i] == s[j]:
                        dp[i][j] = True
                        number_of_substrings += 1
                    else:
                        dp[i][j] = False

        return number_of_substrings