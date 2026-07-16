class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Review
        stack = []
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))
        return sum(stack)