class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        found_val, begin, end = False, 0, len(nums) -1
        

        # Review 1

        '''
        The right side is where all the removed elements are
        The right pointer will receive the removed element
        The left point will receive a substituion
        '''

        
        while begin <= end:
            if nums[begin] == val:
                found_val = True
                # Keep decrementing the right pointer until you see an element not equal to val
                while begin < end and nums[end] == val:
                    end -= 1
                # Swap
                nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1

        # The end pointer is the either the first element of val, or no element of val exists
        '''
        Why does len(nums) work?

        Because it is needed if there is only one element of the same number equal to val
        Or, if val does not exist in the array
        '''
        return end if found_val else len(nums)