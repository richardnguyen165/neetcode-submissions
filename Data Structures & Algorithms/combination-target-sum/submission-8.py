class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Standard backtracking, optimized solution
        # One common array?

        nums.sort()

        # Decision, we stay on this element, or we move to the next one
        all_results = []

        def all_combs(i, current_array, current_sum):
            if i >= len(nums):
                return
            if current_sum == target:
                all_results.append(current_array.copy())
                return
            if current_sum > target:
                return

            # Option 1: Choose this number
            current_array.append(nums[i])
            all_combs(i, current_array, current_sum + nums[i])

            # Option 2: Do not choose this number, go to the next number and decide
            current_array.pop()
            all_combs(i + 1, current_array, current_sum)

        all_combs(0, [], 0)
        return all_results
