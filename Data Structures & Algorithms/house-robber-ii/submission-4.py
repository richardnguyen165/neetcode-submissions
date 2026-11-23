class Solution:
    def rob(self, nums: List[int]) -> int:
        ''' 
        Pretty much all cases involve running two dps,
        either robbing the first house
        or not robbing the first house
        '''
        if len(nums) == 1:
            return nums[0]

        memo =  [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            # We skip to the next house, or we skip two house, and rob this house
            memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or (i == 0)))
            return memo[i][flag]
        # Symbolize robbing the first house, or not robbing the first house
        return max(dfs(0, True), dfs(1, False))