class Solution:
    def rob(self, nums: List[int]) -> int:
        all_results = [0 for  _ in range(len(nums))]
        all_results[0] = nums[0]

        for index in range(1, len(nums)):
            if index == 1:
                all_results[index] = max(nums[0], nums[1])
            else:
                all_results[index] = max(nums[index] + all_results[index - 2], all_results[index - 1])
        print(all_results)
        # Error: Last result could not include the last day
        return max(all_results)