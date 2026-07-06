class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Intuition: The left pointer always lands further than the numbers smaller than the target
        Therefore, the left pointer must always be correct.
        '''

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return left