class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        total_length = len(s)
        first_pointer = 0
        last_pointer = total_length - 1

        while (first_pointer < last_pointer):
            while (first_pointer < total_length and not s[first_pointer].isalnum()):
                first_pointer += 1
            while (last_pointer > -1 and not s[last_pointer].isalnum()):
                last_pointer -= 1
            if (first_pointer < last_pointer and s[last_pointer] != s[first_pointer]):
                return False
            first_pointer += 1
            last_pointer -= 1

        return True