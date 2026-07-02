class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Using solution, as my code worked, but it runtimed out on large test cases (30/32)
        start, end = 0, 0
        
        while end < len(nums):
            nums[start] = nums[end]
            while end < len(nums) and nums[start] == nums[end]:
                end += 1
            start += 1
    
        return start