class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 2 - HashMap
        # O(n) runtime, O(n) space
        freq_counter= {}

        for number in nums:
            if number in freq_counter:
                freq_counter[number] += 1
            else:
                freq_counter[number] = 1 
        
        max_key, max_value = -1, -1
        for key, value in freq_counter.items():
            if value > max_value:
                max_key, max_value = key, value
        
        return max_key