class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        current_xor = nums[0]
        for index in range(1, len(nums)):
            current_xor = current_xor ^ nums[index]
        return current_xor