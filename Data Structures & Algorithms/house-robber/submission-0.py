class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1 House or 2 House

        Thats the only house we can rob, get the max
        (No need to worry about adjacency)
        '''
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        
        '''
        3 House
        Rob 1st and 3rd house, or rob 2nd house
        '''
        all_possibilities = [0 for _ in range(len(nums))]
        all_possibilities[0] =  nums[0]
        all_possibilities[1] =  max(nums[0], nums[1])
        for index in range(2, len(nums)):
            all_possibilities[index] = max(all_possibilities[index - 1], all_possibilities[index - 2] + nums[index])
        return all_possibilities[-1]