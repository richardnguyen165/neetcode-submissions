class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP Approach -> 2D
        longest_palindrome_start = 0
        longest_palindrome_end = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for start_index in range(len(s) - 1, -1, -1):
            print(start_index)
            for end_index in range(start_index, len(s)):
                # Length of 1
                if start_index == end_index:
                    dp[start_index][start_index] = True
                    if (end_index - start_index) > (longest_palindrome_end - longest_palindrome_start):
                        longest_palindrome_start = start_index
                        longest_palindrome_end = end_index
                # Length of 2
                elif end_index == 1 + start_index:
                    if start_index == 2:
                        print(s[start_index], s[end_index], start_index, end_index)
                    dp[start_index][end_index] = s[start_index] == s[end_index]
                    if (end_index - start_index) > (longest_palindrome_end - longest_palindrome_start) and (s[start_index] == s[end_index]):
                        longest_palindrome_start = start_index
                        longest_palindrome_end = end_index
                # Length of >= 3
                else:
                    if dp[start_index + 1][end_index - 1] and s[start_index] == s[end_index]:
                        if (end_index - start_index) > (longest_palindrome_end - longest_palindrome_start):
                            longest_palindrome_start = start_index
                            longest_palindrome_end = end_index
                        dp[start_index][end_index] = True
                    else:
                        # The core is not a palindrome, the outside cannot be a palindrome
                        dp[start_index][end_index] = False


        for d in dp:
            print(d)
        return s[longest_palindrome_start:longest_palindrome_end + 1]