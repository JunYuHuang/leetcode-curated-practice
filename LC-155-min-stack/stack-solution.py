# O(N) T and O(N) S stack solution (NeetCode's modded)
class MinStack:

    def __init__(self):
        self.stack = [] # stores elements of [val, minValAtThisTime]

    def push(self, val: int) -> None:
        lastMin = self.stack[-1][1] if self.stack else val
        self.stack.append([val, min(val, lastMin)])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
