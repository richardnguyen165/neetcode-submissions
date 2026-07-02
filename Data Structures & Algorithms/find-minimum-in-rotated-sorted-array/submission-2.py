class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Ok, we check the end points of the array

        # If the center point we are on is less than the end point we are calculating, we go left

        # If the center point we are on is greater, we go right

        '''
        Example:
        [3,4,5,6,1,2]

        T T T T F F

        We are looking for the first false, that is the first number that is NOT greater than the end point

        or

        [4,5,6,7]

        F F F F
        '''

        begin, end = 0, len(nums) - 1
        min_value = math.inf
        
        while begin <= end:
            mid = begin + ((end - begin) // 2)
            
            if nums[mid] <= nums[len(nums) - 1]:
                end = mid - 1
                min_value = min(min_value, nums[mid])
            elif nums[mid] > nums[len(nums) - 1]:
                begin = mid + 1
        
        return min_value