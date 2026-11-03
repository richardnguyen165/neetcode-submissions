class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_results = []
        all_lists_so_far = {}
        nums.sort()

        def all_combs(current_array, current_sum):
            if current_sum > target:
                return
            if current_sum == target:
                current_array.sort()
                if str(current_array) not in all_lists_so_far:
                    all_lists_so_far[str(current_array)] = ""
                    all_results.append(current_array)

            for num in nums:
                if (current_array and num < max(current_array)):
                    continue
                if (num + current_sum) > target:
                    break
                clone_of_current_array = current_array.copy()
                clone_of_current_array.append(num)
                all_combs(clone_of_current_array, current_sum + num) 

        all_combs([], 0)

        return all_results