class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer, best_length = 0, 0
        for right_pointer in range(0, len(s)):
            current_string = s[left_pointer: right_pointer + 1]
            check_string = set(list(current_string))
            while len(check_string) != len(current_string) and left_pointer <= right_pointer:
                left_pointer += 1
                current_string = s[left_pointer: right_pointer + 1]
                check_string = set(list(current_string))
            best_length = max(best_length, len(current_string))
        return best_length
        