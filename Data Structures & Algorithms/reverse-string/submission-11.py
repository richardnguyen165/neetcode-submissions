class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Stack
        stack = []
        for character in s:
            stack.append(character)
        for index in range(0, len(s)):
            s[index] = stack.pop()