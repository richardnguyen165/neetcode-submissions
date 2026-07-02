class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Idea: Use two pointer approach, one at the beginning, one at the end

        Start from the beginning

        let begin = 0 
        let end = len(nums) -1
        let k = 0

        while (begin < end):
            if nums[begin] == val:
                while (begin < end and nums[end] != val):
                    end -= 1
                # Swap
                let temp = nums[end]
                nums[begin] = temp
                nums[end] = val 
            else:
                k += 1
        
        return k
        '''

        begin = 0 
        end = len(nums) -1
        k = 0

        while (begin < len(nums)):
            print("BEGIN: ", nums, begin, end, nums[begin] == val)
            if nums[begin] == val:
                while (begin < end and nums[end] == val):
                    end -= 1
                # we need to check if there is an acutal value where we can swap, then we can increment
                if (begin < end and nums[end] != val):
                    k += 1
                    # Swap
                    # nums[begin] = nums[end]
                    # nums[end] = val
                    nums[begin], nums[end] = nums[end], nums[begin] 
            else:
                k += 1
            begin += 1
            if begin < len(nums):
                print("END: ", nums, begin, end, nums[begin] == val)
        
        return k