class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_seen_numbers = {}

        for i, n in enumerate(nums):
            other = target - n
            if other in all_seen_numbers:
                return [all_seen_numbers[other], i]
            all_seen_numbers[n] = i