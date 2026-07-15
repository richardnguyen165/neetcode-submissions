class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Review
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # One error, check remaining true or false

                # First check the left option (meaning skip the right error)
                left_s = s[l:r]

                # Then check the right option (meaning skip the left error)
                right_s = s[l + 1 : r + 1]

                if left_s == left_s[::-1]:
                    return True
                elif right_s == right_s[::-1]:
                    return True
                return False
                
        return True