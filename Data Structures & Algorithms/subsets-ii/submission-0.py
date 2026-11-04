class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        all_results = []

        def current_traversal(i, current_arr):
            if i >= len(nums):
                all_results.append(current_arr.copy())
                return

            # Option 1: We choose this number, move to the next number
            current_arr.append(nums[i])
            current_traversal(i + 1, current_arr)

            # Option 2: We do not choose this number, move to the next non same number
            current_arr.pop()
            moving_index = i + 1
            while moving_index < len(nums):
                if nums[moving_index] != nums[i]:
                    current_traversal(moving_index, current_arr)
                    break
                moving_index += 1
            if moving_index == len(nums):
                all_results.append(current_arr.copy())
                return
            
        current_traversal(0, [])
        return all_results