class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Recursirve solution
        
        # Think of sub problems - we are narrowing down the left and the right

        print(s)

        # Cannot swap
        # if len(s) == 0:
        #     return
        # if len(s) == 1:
        #     return
        # s[0], s[-1] = s[-1], s[0]

        # self.reverseString(s[1:-1])
        
        # Slicing creates its own copies, so its not recommended

        def reverse(l, r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            reverse(l + 1, r - 1)
        
        reverse(0, len(s) - 1)