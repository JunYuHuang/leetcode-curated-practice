# My O(N) time and O(N) space stack brute force solution
class MyQueue:
    def __init__(self):
        self.stack = []
        self.revStack = []
    def moveStack(self, src, dst) -> None:
        while src: dst.append(src.pop())
    def push(self, x: int) -> None:
        if not self.stack: self.moveStack(self.revStack, self.stack)
        self.stack.append(x)
    def pop(self) -> int:
        if not self.revStack: self.moveStack(self.stack, self.revStack)
        return self.revStack.pop()
    def peek(self) -> int:
        if not self.revStack: self.moveStack(self.stack, self.revStack)
        return self.revStack[-1]
    def empty(self) -> bool:
        return not self.stack and not self.revStack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()