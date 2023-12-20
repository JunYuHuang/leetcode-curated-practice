# method-dependent T & S stack solution
class BrowserHistory:
    def __init__(self, homepage: str):
        # stack of [index, url] elements
        self.stack = [[0, homepage]]
        self.currPos = 0

    def visit(self, url: str) -> None:
        while self.stack and self.stack[-1][0] > self.currPos:
            self.stack.pop()
        self.stack.append([self.currPos + 1, url])
        self.currPos += 1

    def back(self, steps: int) -> str:
        backSteps = min(self.currPos, steps)
        while backSteps > 0:
            self.currPos -= 1
            backSteps -= 1
        return self.stack[self.currPos][1]

    def forward(self, steps: int) -> str:
        maxSteps = len(self.stack) - 1 - self.currPos
        forwardSteps = min(maxSteps, steps)
        while forwardSteps > 0:
            self.currPos += 1
            forwardSteps -= 1
        return self.stack[self.currPos][1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
