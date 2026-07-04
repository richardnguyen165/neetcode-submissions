class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        Important thing to notice, all the last k elements, 
        become the first k elements

        all the first len(nums) - k elements, become the last
        '''

        # Simple solution: Lots of reversals

        k = k  % len(nums)
        if k == 0:
            return

        # First reverse the entire array

        nums.reverse()

        # Using k:
        nums[:] = nums[:k][::-1] + nums[k:][::-1]


        