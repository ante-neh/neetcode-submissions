class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        curSpan = 1
        while self.stack and self.stack[-1][0] <= price:
            val, span = self.stack.pop()
            curSpan += span

        self.stack.append([price, curSpan])

        return curSpan


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)