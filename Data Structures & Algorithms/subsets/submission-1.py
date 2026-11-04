class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Two choices keep this number, or skip it

        all_results = [[]]

        def all_subsets(i, arr):
            if i == len(nums):
                return
            
            # Option 1
            arr.append(nums[i])
            all_results.append(arr.copy())
            all_subsets(i + 1, arr)

            # Option 2
            arr.pop()
            all_subsets(i + 1, arr)

        all_subsets(0, [])
        return all_results