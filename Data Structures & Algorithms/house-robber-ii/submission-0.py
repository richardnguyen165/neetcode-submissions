class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        no_last = nums[:-1]
        no_first = nums[1:]

        return max(self.rob_helper(no_last), self.rob_helper(no_first))
    
    def rob_helper(self, nums:List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for index in range(2, len(nums)):
            dp[index] = max(nums[index] + dp[index - 2], dp[index - 1])
        
        return dp[-1]