class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        # Error_counter => the amount of letters you can replace (capped at 1)

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                # Use slicing at the first occurance

                # Skip over the left, include the right
                left_option = s[left + 1: right + 1] == s[left + 1: right + 1][::-1]
                
                # Skip over the right, include the left
                right_option = s[left : right] == s[left : right][::-1]

                if left_option:
                    return True
                elif right_option: 
                    return True
                else:
                    return False
        return True