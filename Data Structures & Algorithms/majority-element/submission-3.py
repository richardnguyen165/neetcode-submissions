class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 3 - IMPORTANT: Boyer-Moore Algorithm
        # O(n) runtime, O(1) space

        potential_candidate = count = 0

        for num in nums:
            # Change the candidate
            if count == 0:
                potential_candidate = num
                count += 1
            else:
                if potential_candidate != num:
                    count -= 1
                else:
                    count += 1
        
        return potential_candidate
                
