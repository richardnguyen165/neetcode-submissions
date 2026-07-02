class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_numbers = {}
        for index, num in enumerate(nums):
            other_target = target - num
            if other_target in all_numbers:
                return [all_numbers[other_target], index]
            else:
                all_numbers[num] = index