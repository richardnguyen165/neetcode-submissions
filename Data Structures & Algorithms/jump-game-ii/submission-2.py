import math

class Solution:

    def jump(self, nums: List[int]) -> int:
        # Bottom Up Approach
        dp = [math.inf for _ in range(len(nums))]
        dp[0] = 0

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] != 0 and nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]