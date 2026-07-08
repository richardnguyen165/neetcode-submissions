class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Use hashmap, 
        where the values are the integers we saw,
        and the keys are the last index where we saw them
        '''
        last_seen = {}

        for current_index, number in enumerate(nums):
            if number not in last_seen:
                last_seen[number] = current_index
            else:
                get_index = last_seen[number]

                if abs(get_index - current_index) <= k:
                    return True
                
                last_seen[number] = current_index
        
        return False