class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        begin = 0
        end = len(s) - 1

        while (begin < end):
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1
        
        print(s)