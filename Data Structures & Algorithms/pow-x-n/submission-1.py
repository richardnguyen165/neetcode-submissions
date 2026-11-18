class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = abs(n)

        def power_recurse(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 0:
                result = power_recurse(x, n / 2)
                return result * result
            else:
                result = power_recurse(x, n // 2)
                return result * result * x
            
        return power_recurse(x, n)