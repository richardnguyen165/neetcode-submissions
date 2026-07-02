class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            return []
    
        start_pointer = 0
        all_solutions = []

        for current_index, first_number in enumerate(nums):
            if current_index and nums[current_index - 1] == first_number:
                continue

            start_pointer = current_index + 1
            end_pointer = len(nums) - 1

            while start_pointer < end_pointer:

                total = nums[start_pointer] + nums[end_pointer] + first_number
                
                if total > 0:
                    end_pointer -= 1
                elif total < 0:
                    start_pointer += 1
                else:
                    all_solutions.append([nums[start_pointer], nums[end_pointer], first_number])
                    start_pointer += 1
                    while (nums[start_pointer] == nums[start_pointer - 1] and start_pointer < end_pointer):
                        start_pointer += 1

        return all_solutions