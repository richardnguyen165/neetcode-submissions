class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Bottom up, we exclude first house, 
        or we exclude the last hosue
        '''
        if len(nums) == 1:
            return nums[0]

        def rob_house(current_nums):
            if len(current_nums) == 1:
                return current_nums[0]
            all_results = [0] * len(current_nums)
            if len(current_nums) > 0:
                all_results[0] = current_nums[0]
            if len(current_nums) > 1:
                all_results[1] = max(current_nums[0], current_nums[1])
            
            for i in range(2, len(current_nums)):
                all_results[i] = max(current_nums[i] + all_results[i - 2], all_results[i - 1])

            return max(all_results)
        
        first_result = rob_house(nums[1:])
        second_result = rob_house(nums[:-1])
        return max(first_result, second_result)
            
