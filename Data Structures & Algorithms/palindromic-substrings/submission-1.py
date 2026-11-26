class Solution:
    def countSubstrings(self, s: str) -> int:
        # DP Solution
        
        total_number_of_palindromes = 0
        is_palindromes = [[False] * len(s) for _ in range(len(s))]

        for row_number in range(len(s) - 1, -1, -1):
            for col_number in range(0, len(s)):
                if row_number == col_number:
                    is_palindromes[row_number][col_number] = True
                    total_number_of_palindromes += 1
                elif row_number < col_number and s[row_number] == s[col_number]:
                    # > Two chars
                    if (col_number - 1 > row_number + 1) and is_palindromes[row_number + 1][col_number - 1]:
                        is_palindromes[row_number][col_number] = True
                        total_number_of_palindromes += 1
                    # Two chars
                    elif not (col_number - 1 > row_number + 1):
                        is_palindromes[row_number][col_number] = True
                        total_number_of_palindromes += 1

        return total_number_of_palindromes