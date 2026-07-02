class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonic stack
        final_result = [0] * len(temperatures)
        current_stack = []
        for (day, temp) in enumerate(temperatures):
            print(current_stack)
            if not current_stack:
                current_stack.append([day, temp])
            else:
                current_stack_length = len(current_stack) - 1

                while current_stack and current_stack[current_stack_length][-1] < temp:
                    latest_day = current_stack.pop()
                    final_result[latest_day[0]] = day - latest_day[0]
                    current_stack_length -= 1
                
                current_stack.append([day, temp])
            
        return final_result