class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Solution 2: Use set
        '''

        current_window = set()
        L = 0

        for R in range(len(nums)):
            # If our window is too big, remove leftmost number (or remove the oldest number)
            if R - L > k:
                current_window.remove(nums[L])
                L += 1
            
            # If there is already current duplicate => return True
            if nums[R] in current_window:
                return True
            
            # Add number if there is no duplicate
            current_window.add(nums[R])
        
        return False