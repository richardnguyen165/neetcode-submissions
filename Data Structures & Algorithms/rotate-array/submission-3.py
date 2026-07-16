class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Review

        # Step 0: mod k
        k = k % len(nums)

        # No rotation
        if k == 0:
            return

        # Step 1: Reverse the array
        nums.reverse()

        # Step 2: Using k, create the new nums array
        # print(nums[:k][::-1] + nums[k:][::-1])
        # nums[:] => allows for copy in place
        nums[:] = nums[:k][::-1] + nums[k:][::-1]

