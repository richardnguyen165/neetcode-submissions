class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        lower = 0
        higher = x
        mid = 0

        while lower <= higher:
            mid = (higher + lower) // 2
            print(lower, higher, mid)

            if x == (mid * mid):
                return mid
            elif x < (mid * mid):
                higher = mid - 1
            else:
                lower = mid + 1
    
        return higher