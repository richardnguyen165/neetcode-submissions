class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set()
        for number in nums:
            if number in no_duplicates:
                return True
            no_duplicates.add(number)
        return False
         