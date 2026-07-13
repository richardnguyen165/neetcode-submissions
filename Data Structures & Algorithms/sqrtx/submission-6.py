class Solution:
    def mySqrt(self, x: int) -> int:
        # Using the lower bound as pos candidate
        l, r  = 0, x
        res = 0

        while l <= r:
            mid = l + ((r - l) // 2)

            if mid**2 == x:
                return mid
            elif mid**2 > x:
                r = mid - 1
                res = r
            else:
                l = mid + 1

        return res