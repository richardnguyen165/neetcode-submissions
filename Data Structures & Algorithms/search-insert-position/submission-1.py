class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Basic, naive solution - O(n)
        for index, number in enumerate(nums):
            if number >= target:
                return index
        return len(nums)