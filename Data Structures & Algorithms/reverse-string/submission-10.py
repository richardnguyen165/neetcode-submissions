class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Review 2: Recursive solution

        def reverse_recurse(l: int, r: int, s: List[str]):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            reverse_recurse(l + 1, r- 1, s)

        reverse_recurse(0, len(s) - 1, s)