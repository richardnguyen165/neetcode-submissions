from collections import deque

class StockSpanner:

    # Monotonic stack
    # Sort by highest to lowest, in terms of (price, span)
    '''
    Now how does it solve the index issue?
    Because when you pop the elements that are the lowest, it already does that automatically (since you can't go pas the highest, but you can keep adding the span)
    '''

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        # Monotonic stack
        span = 1

        if not self.stock_stack:
            self.stock_stack.append((price, span))
            return span

        while self.stock_stack and self.stock_stack[-1][0] <= price:
            popped_value = self.stock_stack.pop()
            span += popped_value[1]

        self.stock_stack.append((price, span))
        return span
        




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)