class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1

        while lower <= upper:
            mid = (lower + upper) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                upper = mid - 1

            else:
                lower = mid + 1

        '''
        4 Cases:

        nums[lower] nums[upper] taget

        nums[lower] target nums[upper]

        target nums[lower] nums[upper]

        lower is out of bounds

        upper is out of bounds
        ''' 

        # When the while loop is terminated, it means that upper < lower (flipped roles)

        print(upper, lower)

        if lower >= len(nums) or upper < 0:
            return lower
        elif nums[upper] <= nums[lower] < target:
            return upper + 1
        elif nums[upper] < target < nums[lower]:
            return upper + 1
        else:
            return lower - 1