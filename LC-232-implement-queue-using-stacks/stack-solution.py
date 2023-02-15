# O(1) time and O(N) space stack solution (StefanPochmann's modified)
class MyQueue:
    def __init__(self):
        self.inputStk, self.outputStk = [], []
    def push(self, x: int) -> None:
        self.inputStk.append(x)
    def pop(self) -> int:
        self.peek()
        return self.outputStk.pop()
    def peek(self) -> int:
        if not self.outputStk:
            while self.inputStk: 
                self.outputStk.append(self.inputStk.pop())
        return self.outputStk[-1]
    def empty(self) -> bool:
        return not self.inputStk and not self.outputStk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()