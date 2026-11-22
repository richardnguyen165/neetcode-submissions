class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursive / Top-Down

        cache = {}
        cache[0] = nums[0]
        if len(nums) > 1:
            cache[1]= max(nums[0], nums[1])
        
        def rob_recurse(current_num):
            if current_num in cache:
                return cache[current_num]
            
            result = max(rob_recurse(current_num - 2) + nums[current_num], rob_recurse(current_num - 1))
            cache[current_num] = result
            return result
        
        return rob_recurse(len(nums) - 1)