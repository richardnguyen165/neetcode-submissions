class MinStack:

    def __init__(self):
        self.current_stack = []
        self.current_min = None

    def push(self, val: int) -> None:
        # meaning, stack is empty
        if (self.current_min == None or (val < self.current_min)):
            self.current_min = val
        self.current_stack.append([val, self.current_min])
        print(self.current_stack)

    def pop(self) -> None:
        self.current_stack.pop()
        if (not self.current_stack):
            self.current_min = None
        else:
            self.current_min = self.current_stack[-1][-1]

    def top(self) -> int:
        last_number = self.current_stack[-1]
        print("Top: " + str(self.current_stack[-1][0]))
        return last_number[0]

    def getMin(self) -> int:
        print("Min: " + str(self.current_stack[-1][1]))
        return self.current_stack[-1][1]
