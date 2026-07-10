from collections import deque

class StockSpanner:

    # Monotonic stack
    # Sort by lowest to highest

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        current_lesser_prices = []

        clone_of_stock = self.stock_stack[:]
        count = 0
        while clone_of_stock and clone_of_stock[-1] <= price:
            count += 1
            clone_of_stock.pop()
        
        self.stock_stack.append(price)
        return count + 1
        


        # Acutally don't use the index.
        # Monotonic stack


        




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)