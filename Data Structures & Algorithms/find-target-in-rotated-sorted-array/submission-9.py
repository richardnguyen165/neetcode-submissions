import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First find the cut, so find the min

        start, end, min_index = 0, len(nums) - 1, None
        min_number = math.inf

        if nums[len(nums) - 1] == target:
            return len(nums) - 1
        elif nums[0] == target:
            return 0

        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] <= nums[len(nums) - 1]:
                end = mid - 1
                if min_number != min(min_number, nums[mid]):
                    min_number = min(min_number, nums[mid])
                    min_index = mid
            else:
                start = mid + 1

        print(min_index)
        if min_index != 0:
            if (nums[0] <= target <= nums[min_index - 1]):
                print(0)
                start, end = 0 , min_index - 1
                while start <= end:
                    mid = start + ((end - start) // 2)
                    if target > nums[mid]:
                        start = mid + 1
                    elif target < nums[mid]:
                        end = mid - 1
                    else:
                        return mid
            else:
                print(1)
                start, end = min_index, len(nums) - 1
                while start <= end:
                    mid = start + ((end - start) // 2)
                    if target > nums[mid]:
                        start = mid + 1
                    elif target < nums[mid]:
                        end = mid - 1
                    else:
                        return mid
            return -1
        else:
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + ((end - start) // 2)
                if target > nums[mid]:
                    start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    return mid
            return -1