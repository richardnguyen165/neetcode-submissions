class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        # DP
        all_stairs = [0, 1, 2]
        for number in range(3, n + 1):
            all_stairs.append(all_stairs[number - 1] + all_stairs[number - 2])
        return all_stairs[n]