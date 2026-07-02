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

        if not nums:
            return 0

        begin = 0 
        non_k = 0

        while (begin < len(nums)):
            if nums[begin] == val:
                while (begin < (len(nums) - non_k - 1) and nums[(len(nums) - non_k - 1)] == val):
                    non_k += 1
                if (begin < (len(nums) - non_k - 1) and nums[(len(nums) - non_k - 1)] != val):
                    nums[begin], nums[(len(nums) - non_k - 1)] = nums[(len(nums) - non_k - 1)], nums[begin] 
            begin += 1
        
        return len(nums) if (nums[-1] != val) else len(nums) - non_k - 1