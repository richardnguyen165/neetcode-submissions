class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1 - Sorting approach

        nums.sort()

        # Idea - obviously if it appears the majority, the middle most element is the majority element


        return nums[len(nums) // 2]

