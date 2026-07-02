class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indexes = {}

        for index, number in enumerate(nums):
            other_number = target - number
            if other_number in nums_indexes:
                return sorted([index, nums_indexes[other_number]])
            nums_indexes[number] = index
