class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        is_palindrome = [[False] * len(s) for _ in range(len(s))]

        # A substring != subsequence
        for r in range(len(s) - 1, -1, -1):
            for c in range(0, len(s)):
                # one char long
                # print(r, c, ((r + 1) > (c - 1)))
                if c == r:
                    is_palindrome[r][c] = True
                    if (c - r) > (end - start):
                        start = r
                        end = c
                elif c > r and s[r] == s[c]:
                    # more than two characters long
                    if ((c - 1) > (r + 1)) and is_palindrome[r + 1][c - 1]:
                        is_palindrome[r][c] = True
                        if (c - r) > (end - start):
                            start = r
                            end = c
                    # Two characters long
                    elif not ((c - 1) > (r + 1)):
                        is_palindrome[r][c] = True
                        if (c - r) > (end - start):
                            start = r
                            end = c

        return s[start:end+1]