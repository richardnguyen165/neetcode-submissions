class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointer
            begin_pointer = 0
            last_pointer = len(numbers) - 1

            while (begin_pointer < last_pointer):
                # find the begin_pointer adjacent number via subtraction
                find_number = target - numbers[last_pointer]

                while (begin_pointer < last_pointer and (numbers[begin_pointer] != find_number and numbers[begin_pointer] < find_number)): 
                    begin_pointer += 1

                if (numbers[begin_pointer] == find_number):
                    return [begin_pointer + 1, last_pointer + 1]

                last_pointer -= 1

            return [begin_pointer + 1, last_pointer + 1]
            
            
