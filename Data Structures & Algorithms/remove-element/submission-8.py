class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # What i tried to do at the beginning

        start = 0
        end = len(nums)

        while start < end:
            if nums[start] == val:
                # So that you dont go out of bounds, or replace the element you did before
                end -= 1 
                nums[start] = nums[end]
            else:
                # Ohhh, you need to wait, don't increment right away because you need to check if the swap was valid!!!!
                start += 1
        return end
