class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy implementation

        # Heuristic: Start from the end, find an index and change goal until we reach index  0

        if len(nums) == 1:
            return True
        
        goal = len(nums) - 1

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= goal:
                goal = index
        
        return goal == 0