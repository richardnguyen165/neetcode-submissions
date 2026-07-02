class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_indexes = {}

        for index, number in enumerate(nums):
            nums_indexes[number] = index
        
        for index, number in enumerate(nums):
            other_number = target - number
            if other_number in nums_indexes and nums_indexes[other_number] != index:
                return [index, nums_indexes[other_number]]
