class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_indexed_numbers = {}
        for index, number in enumerate(nums):
            needed_number = target - number
            if needed_number in all_indexed_numbers:
                index_of_needed_number = all_indexed_numbers.get(needed_number)
                indexes = [index, index_of_needed_number]
                indexes.sort()
                return indexes
            all_indexed_numbers[number] = index
        return []