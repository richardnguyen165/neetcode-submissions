class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Two decisions:
        We rob this house and we go 2 steps back, 
        or we rob the house before it

        bottom up, memoization
        '''

        current_result_array = [0] * len(nums)

        current_result_array[0] = nums[0]

        if len(nums) > 1:
            current_result_array[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current_result_array[i] = max(nums[i] + current_result_array[i - 2], current_result_array[i - 1])
        
        return max(current_result_array)