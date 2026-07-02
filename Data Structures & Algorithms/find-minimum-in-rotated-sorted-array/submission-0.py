class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Find the first False (or in the case its not shuffled, the first true)
        
        We will do this by comparing the last value of the array
        
        We do have to worry about the mid part being equal to the last part, if the array is size of two**
        
        If we have a value that is greater than the end point, it means that the array has shifted
        Thus, we will move to the left, to ensure we get to the end part
        
        If we have a value that is less OR EQUAL than the end point, move to the right
        '''
        left, right, last_number, small = 0, len(nums) - 1, nums[-1], None
        while left <= right:
            mid = left + (right - left) // 2
            if small == None:
                small = nums[mid]
            # If we have a value that is less than the end point, move to the right (possible small value)
            if nums[mid] <= nums[-1]:
                small = nums[mid]
                right = mid - 1
            # If we have a value that is greater than the end point, it means that the array has shifted
            # Thus, we will move to the left, to ensure we get to the end part (no change in small value)
            else:
                left = mid + 1
        return small
        